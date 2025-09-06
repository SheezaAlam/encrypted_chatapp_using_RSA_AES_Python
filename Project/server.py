import socket
import struct
import sys
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding as rsa_padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ---- Framing helpers: send/receive [4-byte length][payload] ----
def send_frame(conn: socket.socket, data: bytes) -> None:
    conn.sendall(struct.pack("!I", len(data)) + data)

def recv_frame(conn: socket.socket) -> bytes:
    header = b""
    while len(header) < 4:
        chunk = conn.recv(4 - len(header))
        if not chunk:
            return b""
        header += chunk
    (length,) = struct.unpack("!I", header)

    payload = b""
    while len(payload) < length:
        chunk = conn.recv(length - len(payload))
        if not chunk:
            return b""
        payload += chunk
    return payload

# ---- 1) Server RSA keypair (2048-bit) ----
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# ---- 2) TCP server ----
HOST, PORT = "127.0.0.1", 5555
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
srv.listen(1)
print(f"✅ Server listening on {HOST}:{PORT} ...")

conn, addr = srv.accept()
print(f"🎉 Client connected from {addr}")

# ---- 3) Send RSA public key to client ----
send_frame(conn, public_pem)
print("🔑 Sent RSA public key to client.")

# ---- 4) Receive AES key (RSA-OAEP encrypted) and decrypt ----
enc_aes_key = recv_frame(conn)
if not enc_aes_key:
    print("❗ Client disconnected before key exchange.")
    conn.close(); srv.close(); sys.exit(0)

aes_key = private_key.decrypt(
    enc_aes_key,
    rsa_padding.OAEP(
        mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"✅ AES session key established ({len(aes_key)*8}-bit).")
aesgcm = AESGCM(aes_key)

print("💬 Secure chat ready. Type 'exit' to quit.")

try:
    while True:
        # ---- 5) Receive encrypted message: [12-byte nonce][ciphertext+tag] ----
        packet = recv_frame(conn)
        if not packet:
            print("👋 Client disconnected."); break
        if len(packet) < 12:
            print("❗ Malformed packet."); break

        nonce = packet[:12]
        ciphertext = packet[12:]
        try:
            plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None).decode("utf-8")
        except Exception as e:
            print(f"❗ Decryption failed: {e}"); break

        print(f"👤 Client: {plaintext}")

        # ---- 6) Read reply, encrypt, send ----
        reply = input("You: ")
        nonce_out = os.urandom(12)
        ciphertext_out = aesgcm.encrypt(nonce_out, reply.encode("utf-8"), None)
        send_frame(conn, nonce_out + ciphertext_out)

        if reply.strip().lower() == "exit":
            break

finally:
    conn.close()
    srv.close()
    print("🔒 Server closed.")
