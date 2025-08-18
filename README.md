# 🔐 Encrypted Chat App (Python, RSA + AES-GCM)
 
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![AES](https://img.shields.io/badge/Encryption-AES-green)
![RSA](https://img.shields.io/badge/Encryption-RSA-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


A simple end-to-end encrypted chat using:
- **RSA-OAEP** to exchange an AES session key
- **AES-GCM** to encrypt each message (confidentiality + integrity)
- **TCP sockets** for real-time chat
- **Length-prefixed frames** so messages aren’t cut

  # 📦 Encrypted-Chat-App 
┣ 📜 server.py # Server code (handles clients, RSA + AES setup) 
┣ 📜 client.py # Client code (connects to server, sends/receives encrypted messages) 
┣ 📜 requirements.txt # Dependencies 
┗ 📜 README.md # Documentation

## ✅ Features
- RSA public key sent from server → client
- Client generates random AES key → encrypts with RSA → sends to server
- Both sides chat using AES-GCM with fresh nonces per message
- Works on any OS with Python 3.10+

## 🧰 Tech
`Python 3.10+`, `cryptography`, `sockets`

## ▶️ Run  
pip install -r requirements.txt
python server.py
# In another terminal:
python client.py

Type messages on each side. Use exit to close.

## ⚠️ Notes (for learning) 

Never reuse the same (key, nonce) pair in GCM.

This demo is single client and not authenticated by identity (no certificates).

For production, add: persistent RSA keys, client auth, multiple clients (threads/async), ECDH for forward secrecy.

## 📜 License

MIT


