from flask import Flask, render_template, request
import hashlib
import requests
import math
import os
import re  

app = Flask(__name__)

# ---------- Password Strength Checker ----------
def check_strength(password):
    score = 0
    reasons = []

    if len(password) >= 12:
        score += 2
    else:
        reasons.append("Too short (min 12 characters)")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        reasons.append("No digits")

    if any(char.isupper() for char in password):
        score += 1
    else:
        reasons.append("No uppercase letters")

    if any(char in '!@#$%^&*()_+-=[]{};:\'",.<>?/|' for char in password):
        score += 1
    else:
        reasons.append("No special characters")

    if password.lower() in ['password', '123456', 'admin']:
        score = 0
        reasons.append("Common password")

    # New: Check for repetitive sequences > 3
    if re.search(r'(?:\d{4,})', password):
        reasons.append("Too many digits in a row")

    if re.search(r'(?:[a-zA-Z]{4,})', password):
        reasons.append("Too many letters in sequence")

    if re.search(r'([!@#$%^&*()_+\-=\[\]{};:\'",.<>?/|])\1{3,}', password):
        reasons.append("Too many repeated special characters")

    # Classification
    if score >= 5 and not reasons:
        return "Very Strong", []
    elif score >= 4:
        return "Strong", reasons
    else:
        return "Weak", reasons

# ---------- Entropy Calculator ----------
def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in '!@#$%^&*()_+-=[]{};:\'",.<>?/|' for c in password): charset += 32
    if charset == 0:
        return 0.0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

# ---------- Breach Checker (HIBP) ----------
def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    try:
        res = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
        hashes = res.text.splitlines()
        return any(line.startswith(suffix) for line in hashes)
    except:
        return False

# ---------- Routes ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        password = request.form['password']
        result['strength'], result['reasons'] = check_strength(password)
        result['breached'] = check_breach(password)
        result['entropy'] = calculate_entropy(password)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
