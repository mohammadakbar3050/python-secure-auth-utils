import random
import secrets
import string


class PasswordGenerator:
    """password generation
    - Basic generation
    - Secure generation"""

    def __init__(self, length: int = 10, special: bool = False, digits: bool = False):
        self.length = length
        self.special = special
        self.digits = digits

    def _build_chars(self) -> str:
        chars = string.ascii_letters
        if self.digits:
            chars += string.digits
        if self.special:
            chars += string.punctuation
        return chars

    def generate(self) -> str:
        """
        Docstring for generete

        - For basic password generation
        - Using random module : random.choice
        """
        chars = self._build_chars()
        return "".join(random.choice(chars) for _ in range(self.length))

    def generate_secure(self) -> str:
        """
        Docstring for generate_secure

        - For secure password generation
        - Using secrets module : secrets.choice
        """
        chars = self._build_chars()
        return "".join(secrets.choice(chars) for _ in range(self.length))
