import unittest
from project.otp_generator import OTPGenerator


class TestOTPGenerator(unittest.TestCase):

    def test_otp_length(self):
        otp = OTPGenerator(length=6)
        result = otp.generate()
        self.assertEqual(len(result), 6)

    def test_otp_digits_only(self):
        otp = OTPGenerator(length=6)
        result = otp.generate()
        self.assertTrue(result.isdigit())

    def test_secure_otp_length(self):
        otp = OTPGenerator(length=8)
        result = otp.generate_secure()
        self.assertEqual(len(result), 8)


if __name__ == "__main__":
    unittest.main()