import socket
import struct
import sys
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
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

# ---- 1) Connect to server ----
HOST, PORT = "127.0.0.1", 5555
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((HOST, PORT))
print(f"✅ Connected to server at {HOST}:{PORT}")

# ---- 2) Receive server RSA public key ----
server_pub_pem = recv_frame(cli)
if not server_pub_pem:
    print("❗ Failed to receive server public key."); cli.close(); sys.exit(0)

server_public_key = serialization.load_pem_public_key(server_pub_pem)
print("🔑 Received server RSA public key.")

# ---- 3) Generate AES key (AES-256) and send encrypted with RSA-OAEP ----
aes_key = os.urandom(32)  # 32 bytes = 256-bit
aesgcm = AESGCM(aes_key)

enc_key = server_public_key.encrypt(
    aes_key,
    rsa_padding.OAEP(
        mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
send_frame(cli, enc_key)
print("✅ Sent AES session key encrypted with RSA.")

print("💬 Secure chat ready. Type 'exit' to quit.")

try:
    while True:
        # ---- 4) Read your message, encrypt with AES-GCM, send ----
        msg = input("You: ")
        nonce = os.urandom(12)  # Unique per message
        ciphertext = aesgcm.encrypt(nonce, msg.encode("utf-8"), associated_data=None)
        send_frame(cli, nonce + ciphertext)

        if msg.strip().lower() == "exit":
            break

        # ---- 5) Receive server reply, decrypt, print ----
        packet = recv_frame(cli)
        if not packet:
            print("👋 Server disconnected."); break
        if len(packet) < 12:
            print("❗ Malformed packet."); break

        nonce_in = packet[:12]
        ciphertext_in = packet[12:]
        try:
            reply = aesgcm.decrypt(nonce_in, ciphertext_in, associated_data=None).decode("utf-8")
        except Exception as e:
            print(f"❗ Decryption failed: {e}"); break

        print(f"👤 Server: {reply}")

        if reply.strip().lower() == "exit":
            break

finally:
    cli.close()
    print("🔒 Client closed.")
