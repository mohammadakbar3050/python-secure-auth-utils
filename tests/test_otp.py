from project.otp_generator import OTPGenerator


def test_otp_length():
    otp = OTPGenerator(length=6)
    assert len(otp.generate()) == 6


def test_otp_with_digits():
    otp = OTPGenerator(length=6)
    assert otp.generate().isdigit()


def test_secure_length():
    otp = OTPGenerator(length=6)
    assert len(otp.generate_secure()) == 6


def test_secure_with_digits():
    otp = OTPGenerator(length=6)
    assert otp.generate_secure().isdigit()
