from faker import Faker
import random
import string

from userinyerface.models.schemas import UserFields


class FakeUserFactory:
    _faker = Faker()

    @classmethod
    def _generate_valid_password(cls, email: str, length: int = 12) -> str:

        latin_letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        email_letters = [ch for ch in email if ch.isalpha()]
        email_letter = random.choice(email_letters)

        password_chars = [
            random.choice(string.ascii_uppercase),
            random.choice(digits),
            email_letter,
            random.choice(special_chars),
        ]

        all_chars = latin_letters + digits + special_chars
        while len(password_chars) < length:
            password_chars.append(random.choice(all_chars))

        random.shuffle(password_chars)
        return ''.join(password_chars)

    @classmethod
    def create(cls) -> UserFields:
        email = cls._faker.email()
        domain = email.split("@")[1].split(".")[0]
        domain_zone = random.choice(["com", "net", "org", "de"])
        password = cls._generate_valid_password(email)

        return UserFields(
            email=email,
            password=password,
            domain=domain,
            domain_zone=domain_zone
        )