from project.password_generator import PasswordGenerator


def test_password_length():
    pw = PasswordGenerator(length=15)
    assert len(pw.generate()) == 15


def test_password_with_digits():
    pw = PasswordGenerator(length=15, digits=True)
    assert any(char.isdigit() for char in pw.generate())


def test_secure_password_length():
    pw = PasswordGenerator(length=15)
    assert len(pw.generate()) == 15


def test_secure_password_with_digits():
    pw = PasswordGenerator(length=15, digits=True)
    assert any(char.isdigit() for char in pw.generate_secure())
