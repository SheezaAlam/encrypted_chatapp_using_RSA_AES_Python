
```markdown
# 🔐 Encrypted Chat App

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![AES](https://img.shields.io/badge/Encryption-AES-green)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
[![RSA](https://img.shields.io/badge/Encryption-RSA-orange)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/SheezaAlam/Encrypted-Chat-App?style=social)](https://github.com/SheezaAlam/Encrypted-Chat-App/stargazers)

A simple **end-to-end encrypted chat application** built with **Python sockets**, **AES**, and **RSA**.  
This project demonstrates how secure communication works in real-time over the network.

---

## 🚀 Features
- ✅ **AES Encryption** for fast and secure message transfer  
- ✅ **RSA Encryption** for exchanging AES keys securely  
- ✅ **Real-time Chat** using Python sockets  
- ✅ **Cross-platform** (works on any OS with Python installed)  

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **AES (Symmetric Encryption)**
- **RSA (Asymmetric Encryption)**
- **Socket Programming**

---

## 📂 Project Structure
```

📦 Encrypted-Chat-App
┣ 📜 server.py   # Server code (handles clients, RSA + AES setup)
┣ 📜 client.py   # Client code (connects to server, sends/receives encrypted messages)
┣ 📜 requirements.txt # Dependencies
┗ 📜 README.md   # Documentation

````

---

## ⚡ Quick Start

1️⃣ Clone the repo  
```bash
git clone https://github.com/SheezaAlam/Encrypted-Chat-App.git
cd Encrypted-Chat-App
````

2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

3️⃣ Start the server

```bash
python server.py
```

4️⃣ Open another terminal and run the client

```bash
python client.py
```

5️⃣ Start chatting securely! 🎉

---

## 📖 How It Works

* 🗝 **RSA** is used to securely exchange an AES session key.
* 🔑 **AES** then encrypts/decrypts chat messages in real time.
* 📡 Messages travel encrypted over the network — even if intercepted, they can’t be read.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

