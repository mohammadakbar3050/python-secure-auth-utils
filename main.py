from project.otp_generator import OTPGenerator
from project.password_generator import PasswordGenerator
from project.utils import banner


def main() -> None:
    banner("OTP GENERATION")

    otp = OTPGenerator(length=6)
    print(f"OTP (basic) : {otp.generate()}")
    print(f"OTP (secured) : {otp.generate_secure()}")
    banner("PASSWORD GENERATION")

    password = PasswordGenerator(length=10)
    print(f"PASSWORD GENERATED (basic) : {password.generate()}")
    print(f"PASSWORD GENERATED (secured) : {password.generate_secure()}")


def strong_pw_gen() -> None:
    password = PasswordGenerator(length=15, special=True, digits=True)
    banner("STRONG PASSWORD GENERATION")
    print(f"STRONG PASSWORD GENERATED (basic) : {password.generate()}")
    print(f"STRONG PASSWORD GENERATED (secured) : {password.generate_secure()}")


if __name__ == "__main__":
    main()
    strong_pw_gen()
