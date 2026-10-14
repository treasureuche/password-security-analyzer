
![Python Tests](https://github.com/treasureuche/password-security-analyzer/actions/workflows/main.yml/badge.svg)

# 🔐 Password Security Analyzer

A beginner-friendly cybersecurity project built with Python that evaluates password strength and provides personalized security recommendations.

## 📌 About the Project

This project demonstrates fundamental Python programming concepts and basic password security principles.

The analyzer evaluates passwords against five requirements and provides feedback to help users create stronger passwords.

## ✨ Features

- Checks password length
- Detects uppercase and lowercase letters
- Checks for numbers and special characters
- Calculates a password strength score out of 5
- Classifies passwords as Weak, Medium, or Strong
- Provides personalized improvement suggestions
- Hides password input using Python's getpass module

## 🛠️ Technologies Used

- Python 3
- Visual Studio Code
- Python Standard Library

## 🚀 How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

   py password-analyzer.py

   Alternatively, use:
   
   python password-analyzer.py

5. Enter a test password and review the results.

## 📊 Strength Scoring

| Score | Rating |
|-------|--------|
| 0–2 | Weak |
| 3–4 | Medium |
| 5 | Strong |

## 🔒 Security Considerations

- Passwords are not intentionally saved to files.
- Password input is hidden using getpass.
- Password strength is evaluated using basic rules.
- A high score does not guarantee password security.
- Avoid testing real passwords in untrusted environments.

## 🔮 Future Improvements

- Detect commonly used passwords
- Estimate password strength using more advanced methods
- Add automated unit tests
- Build a graphical user interface
- Explore secure cloud deployment

## 👩🏽‍💻 Author

Treasure Uchechukwu Ihedioha

Information Technology Undergraduate

Interests: Cybersecurity | Cloud Engineering | Artificial Intelligence | Software Development

## Automated Testing

This project includes automated unit tests using Python's built-in `unittest` framework.

The tests verify:
- Weak password detection
- Common password detection
- Medium-strength password detection
- Strong password detection

### Run the Tests

```bash
py -m unittest test_password_utils.py -v
```

All four tests passed successfully during local testing.

## Project Structure

- `password-analyzer.py` - Main application
- `password_utils.py` - Password strength analysis function
- `test_password_utils.py` - Automated unit tests
- `README.md` - Project documentation
