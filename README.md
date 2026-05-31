# 🔐 Password Strength & Entropy Checker

A lightweight Python CLI tool that analyzes password strength, estimates entropy, and provides security recommendations. This project is designed for cybersecurity professionals, students, and anyone interested in understanding password security fundamentals.

---

## 📖 Overview

Passwords are often the first line of defense against unauthorized access. Weak passwords can be cracked through brute-force attacks, dictionary attacks, or credential stuffing.

The Password Strength & Entropy Checker helps users evaluate the security of their passwords by analyzing:

- Password length
- Character diversity
- Entropy estimation
- Overall strength rating
- Security improvement suggestions

This tool is intended for educational purposes, cybersecurity awareness programs, and password policy demonstrations.

---

## ✨ Features

### 🔍 Password Analysis
- Checks password length
- Detects character variety
- Evaluates password complexity

### 📊 Entropy Calculation
- Estimates password entropy using standard mathematical formulas
- Helps demonstrate resistance against brute-force attacks

### 🛡️ Strength Classification
Classifies passwords into categories such as:

- Very Weak
- Weak
- Moderate
- Strong
- Very Strong

### 💡 Security Recommendations
Provides suggestions to improve password security.

### ⚡ Lightweight
- No external dependencies
- Pure Python implementation
- Fast execution

---

## 🛠 Requirements

- Python 3.8+
- No third-party libraries required

Verify your Python installation:

```bash
python --version
```

---

## 📂 Project Structure

```text
password-strength-checker/
│
├── password_checker.py
├── README.md
└── LICENSE
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/password-strength-checker.git
```

### Navigate to the Project Directory

```bash
cd password-strength-checker
```

---

## ▶️ Usage

Run the application:

```bash
python password_checker.py
```

Enter a password when prompted:

```text
Enter password: MySecure@Password123
```

Example output:

```text
Password Analysis
------------------
Length: 20
Lowercase Letters: Yes
Uppercase Letters: Yes
Numbers: Yes
Special Characters: Yes

Estimated Entropy: 131.2 bits

Strength: Very Strong

Recommendations:
✓ Excellent password strength
```

---

## 📊 Entropy Calculation

Entropy measures the unpredictability of a password.

The tool uses the formula:

```text
Entropy = Password Length × log₂(Character Set Size)
```

### Example

Password:

```text
MySecure@Password123
```

Character Sets Used:

- Lowercase letters (26)
- Uppercase letters (26)
- Numbers (10)
- Special characters (32)

Total Character Set Size:

```text
94
```

Entropy:

```text
20 × log₂(94)
≈ 131.2 bits
```

Higher entropy generally indicates stronger protection against brute-force attacks.

---

## 🔒 Password Strength Levels

| Entropy (Bits) | Strength |
|---------------|----------|
| < 28 | Very Weak |
| 28 - 35 | Weak |
| 36 - 59 | Moderate |
| 60 - 127 | Strong |
| ≥ 128 | Very Strong |

---

## 📸 Sample Outputs

### Weak Password

```text
Enter password: password123

Password Analysis
------------------
Length: 11
Lowercase Letters: Yes
Uppercase Letters: No
Numbers: Yes
Special Characters: No

Estimated Entropy: 37.2 bits

Strength: Weak

Recommendations:
- Add uppercase letters
- Add special characters
- Increase password length
```

### Strong Password

```text
Enter password: C0mpl3x!Secure#Pass2025

Password Analysis
------------------
Length: 24
Lowercase Letters: Yes
Uppercase Letters: Yes
Numbers: Yes
Special Characters: Yes

Estimated Entropy: 157.3 bits

Strength: Very Strong

Recommendations:
✓ Excellent password strength
```

---

## 🎯 Use Cases

### Cybersecurity Awareness
Demonstrate the importance of strong passwords.

### Security Training
Help employees understand password security best practices.

### Educational Projects
Learn about entropy, brute-force attacks, and password complexity.

### Password Policy Validation
Test passwords against organizational security standards.

---

## 🔐 Password Security Best Practices

- Use at least 12–16 characters
- Mix uppercase and lowercase letters
- Include numbers and special characters
- Avoid common words and phrases
- Avoid personal information
- Use a unique password for every account
- Enable Multi-Factor Authentication (MFA)
- Consider using a password manager

---

## 🚧 Future Enhancements

Planned improvements include:

- Password breach database checking
- Password generation feature
- Common password blacklist detection
- NIST password policy validation
- Export reports to CSV or JSON
- GUI version using Tkinter
- Web application version

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

### 🔐 Strong Passwords Are Your First Line of Defense.
### 🚀 Stay Secure. Stay Protected.
