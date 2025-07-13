# 🔐 Smart Password Auditor (Web UI)

This is the **Version 2** of the **Smart Password Auditor**, now with a sleek and interactive web interface built using **Flask**.

> ✅ Checks password strength  
> ✅ Verifies if it's been breached using the HaveIBeenPwned API  
> ✅ Calculates entropy  
> ✅ Explains why a password is weak  
> ✅ Warns users not to test real passwords

---

## 🚀 Features

- **Strength Evaluation**: Flags weak vs strong passwords.
- **Breach Check**: Queries live breach data from HaveIBeenPwned using [k-Anonymity](https://haveibeenpwned.com/API/v3#PwnedPasswords).
- **Entropy Estimation**: Displays the estimated entropy in bits.
- **Weakness Feedback**: Tells you what’s missing (no digits, uppercase, special chars, etc.)
- **Modern UI**: Includes show/hide password feature, color-coded feedback, and warning banner.

---

## 🖼️ Screenshot


---

## 🛠️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Nissiuser/smart-password-auditor.git
cd smart-password-auditor

# 2. Checkout the Web UI version
git checkout -b v2-web-ui

# 3. (Optional but recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Linux/Mac: source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
