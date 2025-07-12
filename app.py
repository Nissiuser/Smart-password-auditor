import hashlib
import requests
import math
from colorama import Fore, Style

def check_strength(password):
    score = 0
    if len(password) >= 12: score += 2
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c in '!@#$%^&*' for c in password): score += 1
    if password.lower() in ['password', '123456']: score = 0
    return "Weak" if score < 3 else "Strong"

def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    return any(line.startswith(suffix) for line in response.text.splitlines())

def entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password): charset += 32
    return round(len(password) * math.log2(charset), 2) if charset else 0

if __name__ == "__main__":
    print("Script started")  # Add this at the top of if __name__ == "__main__"
    password = input("Test a password: ")
    print("⚠️ Don't use real passwords for testing.")

    strength = check_strength(password)
    breached = check_breach(password)
    entropy_score = entropy(password)

    color = Fore.GREEN if strength == "Strong" else Fore.RED
    print(f"Strength: {color}{strength}{Style.RESET_ALL}")
    print(f"Breached: {Fore.RED if breached else Fore.GREEN}{'YES' if breached else 'NO'}{Style.RESET_ALL}")
    print(f"Entropy Score: {Fore.CYAN}{entropy_score} bits{Style.RESET_ALL}")
