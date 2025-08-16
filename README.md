
```markdown
# 🔐 Encrypted Chat Application  

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  
[![Crypto](https://img.shields.io/badge/Security-AES%20%7C%20RSA-green?logo=hackaday)](https://en.wikipedia.org/wiki/Public-key_cryptography)  
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Stars](https://img.shields.io/github/stars/yourusername/encrypted-chat?style=social)](https://github.com/yourusername/encrypted-chat/stargazers)  
[![Issues](https://img.shields.io/github/issues/yourusername/encrypted-chat)](https://github.com/yourusername/encrypted-chat/issues)  

A simple end-to-end encrypted chat application built in **Python** using **sockets** for networking and **AES + RSA** for encryption.  
This project demonstrates the basics of **secure communication protocols** — including key exchange, message encryption, and safe client-server interaction.

---

## ✨ Features
- 🔑 **RSA** used for exchanging encryption keys securely  
- 🔒 **AES** used for fast and secure message encryption  
- 💬 Real-time encrypted chat between client and server  
- 🖥️ Command-line based, lightweight, and easy to run  

---

## 📂 Project Structure
```

encrypted-chat/
│── server.py       # Server code (receives connections and messages)
│── client.py       # Client code (connects to server, sends/receives messages)
│── README.md       # Project documentation

````

---

## ⚡ How It Works
1. The **server** generates RSA keys (public & private).  
2. The **client** requests the public key and uses it to encrypt a randomly generated AES session key.  
3. The server decrypts the AES key using its RSA private key.  
4. All chat messages are encrypted using AES before being sent.  
5. Both sides can now chat securely, with messages unreadable to eavesdroppers.  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x  
- `pycryptodome` library (for AES & RSA)  

Install dependencies:
```bash
pip install pycryptodome
````

### Running the Chat

1. Start the server:

```bash
python server.py
```

2. In another terminal, run the client:

```bash
python client.py
```

3. Start chatting securely! 🔐

---

## 📖 Learning Objectives

This project will help you understand:

* How socket programming works in Python
* The role of **RSA** in secure key exchange
* Why **AES** is used for actual message encryption (fast & secure)
* Basics of designing an **encrypted communication system**

---

## 🤝 Contributions

Feel free to fork this repo, improve the code (e.g., add GUI, multiple clients, or file transfer), and submit pull requests!

---

## 🛡️ Disclaimer

This project is for **educational purposes only** and should not be used in production systems.

```

Do you want me to **make the badges appear in one line (row)** instead of stacked vertically? That looks even more **pro-level**.
```
