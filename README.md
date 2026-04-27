# Secure Auth Utils 🔐

A modular Python utility package for generating secure OTPs and passwords.
Designed with clean architecture, testability, and extensibility in mind.

This project demonstrates secure randomness handling, structured package
design, and unit testing using pytest.

---

## ✨ Features

- Numeric OTP generation (configurable length)
- Cryptographically secure OTP generation using Python's `secrets` module
- Configurable password generation (length, digits, special characters)
- Clean separation of orchestration and business logic
- Modular package structure
- Unit testing with `pytest`

---

## 🗂 Project Structure

```text
secure-auth-utils/
│
├── main.py                  # Entry point / orchestration
├── project/                 # Core logic (package)
│   ├── otp_generator.py
│   ├── password_generator.py
│   ├── utils.py
│   └── __init__.py
│
├── tests/                   # Unit tests
│   ├── test_otp.py
│   ├── test_password.py
│   └── __init__.py
│
└── .gitignore
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧪 Run Tests

```bash
pytest tests/ -v
```

---

## 🧪 Testing Coverage

Current tests validate (8 tests total):

- OTP length correctness
- OTP digit-only validation
- Secure OTP length correctness
- Secure OTP digit-only validation
- Password length validation
- Password digit inclusion (`digits=True`)
- Secure password length validation
- Secure password digit inclusion (`digits=True`)

---

## 🧠 Design Principles

- `main.py` handles execution only (no business logic)
- Core functionality lives inside a reusable package (`project/`)
- Secure randomness implemented using Python's `secrets` module
- Structure follows scalable Python package conventions
- Logic is written to be testable and modular

---

## 📌 Future Improvements

- Add guaranteed digit inclusion when `digits=True` is enabled
- Expand tests with invalid and boundary input cases
- Add CLI support using `argparse`
- Implement strict input validation for OTP and password length
- Add configurable maximum length safeguards
- Support custom character sets (alphanumeric, symbols)
- Convert to `src/` layout for packaging and distribution

---

## 📄 License

This project is for educational and portfolio purposes.
