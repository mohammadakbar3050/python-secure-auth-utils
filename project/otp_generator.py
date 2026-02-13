import random
import string
import secrets


class OTPGenerator:
    """
    Docstring for OTPGenerator
    - basic genertor
    - secure encrypted generator
    """

    def __init__(self, length=6):
        self.length = length

    def generate(self) -> str:
        """
        Docstring for generate
        - Generated using random.choice --usually not secure
        """
        return "".join(random.choice(string.digits) for _ in range(self.length))

    def generate_secure(self) -> str:
        """
        Docstring for generate_secure
        - Using secrets.choice --secured and encrypted
        """
        return "".join(secrets.choice(string.digits) for _ in range(self.length))
