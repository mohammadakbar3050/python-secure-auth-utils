import random
import string
import secrets


class OTPGenerator:
    """
    Generate basic and secure OTPs.

    Provides:
    - Basic generator using random (not secure)
    - Secure generator using secrets (CSPRNG)
    """

    def __init__(self, length: int = 6) -> None:
        self.length = length

    def generate(self) -> str:
        """
        Docstring for generate
        - using random.choice --usually not secure
        """
        return "".join(random.choice(string.digits) for _ in range(self.length))

    def generate_secure(self) -> str:
        """
        Docstring for generate_secure
        - Using secrets.choice for cryptographically secure randomness
        """
        return "".join(secrets.choice(string.digits) for _ in range(self.length))
