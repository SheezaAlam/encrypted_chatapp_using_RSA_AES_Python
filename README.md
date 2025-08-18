# 🔐 Encrypted Chat App (Python, RSA + AES-GCM)

A simple end-to-end encrypted chat using:
- **RSA-OAEP** to exchange an AES session key
- **AES-GCM** to encrypt each message (confidentiality + integrity)
- **TCP sockets** for real-time chat
- **Length-prefixed frames** so messages aren’t cut

## ✅ Features
- RSA public key sent from server → client
- Client generates random AES key → encrypts with RSA → sends to server
- Both sides chat using AES-GCM with fresh nonces per message
- Works on any OS with Python 3.10+

## 🧰 Tech
`Python 3.10+`, `cryptography`, `sockets`

## ▶️ Run
```bash
pip install -r requirements.txt
python server.py
# in another terminal:
python client.py
