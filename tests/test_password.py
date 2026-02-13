import unittest
from project.password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        pw = PasswordGenerator(length=12)
        result = pw.generate()
        self.assertEqual(len(result), 12)

    def test_password_with_digits(self):
        pw = PasswordGenerator(length=12, digits=True)
        result = pw.generate()
        self.assertTrue(any(char.isdigit() for char in result))

    def test_secure_password_length(self):
        pw = PasswordGenerator(length=15)
        result = pw.generate_secure()
        self.assertEqual(len(result), 15)


if __name__ == "__main__":
    unittest.main()
