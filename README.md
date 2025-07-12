# 🔐 Smart Password Auditor (CLI)

A simple command-line tool to check:

- Password strength
- Whether it has been found in a data breach (via HaveIBeenPwned API)
- Password entropy score (bit-based)

## 💻 How to Run

1. Clone this repo:
git clone https://github.com/Nissiuser/smart-password-auditor.git

2. Go inside the folder and install requirements:
cd smart-password-auditor
pip install -r requirements.txt

3. Run the tool:
python app.py

## 🧠 Features

- Color-coded password strength
- Checks against real-world breach data using k-Anonymity (via [PwnedPasswords API](https://haveibeenpwned.com/API/v3#PwnedPasswords))
- Entropy calculation in bits

## ⚠️ Disclaimer

Do not use real passwords. This tool is for **learning purposes only**.

---

by **Nissi Dasari**