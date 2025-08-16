# 🔐 Encrypted Chat App (Python + RSA + AES)

A simple **end-to-end encrypted chat application** built with Python using **RSA** for key exchange and **AES** for message encryption.  
This project demonstrates how secure communication protocols work at a basic level.

---

## ✨ Features
- Secure **RSA (2048-bit)** key exchange.
- Fast **AES (128-bit)** symmetric encryption for chat messages.
- Real-time encrypted communication between server and client.
- Educational and beginner-friendly Python implementation.

---

## 🛠️ Tech Stack
- **Python 3**
- **RSA (pycryptodome / rsa library)**
- **AES (ECB mode, for demo purposes)**
- **Sockets**

---

## 🚀 Usage

### 1️⃣ Run the Server
```bash
python server.py

### 2️⃣ ***Run the Client***
python client.py

3️⃣ Start Chatting

Type a message on client or server.

Messages are encrypted before sending and decrypted after receiving.

⚠️ Note

This project is for educational purposes only.

AES in ECB mode is not secure in real-world applications (use CBC or GCM).

For real-world secure communication, always rely on trusted libraries like TLS/SSL.


