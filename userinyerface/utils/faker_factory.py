import random
from typing import Optional, List

from faker import Faker

from userinyerface.models.schemas import UserFields


class FakeUserFactory:
    _faker = Faker()

    @classmethod
    def _generate_password(
            cls,
            *,
            length,
            special_chars,
            digits,
            upper_case,
            lower_case,
            text: Optional[str] = None,
    ):
        if text:
            letters = [c for c in text if c.isalpha()]
            if letters:
                base = cls._faker.password(
                    length=length - 1,
                    special_chars=special_chars,
                    digits=digits,
                    upper_case=upper_case,
                    lower_case=lower_case,
                )
                base += random.choice(letters)
                return base
        return cls._faker.password(
            length=length,
            special_chars=special_chars,
            digits=digits,
            upper_case=upper_case,
            lower_case=lower_case,
        )

    @classmethod
    def create(
            cls,
            *,
            password_length: int = 10,
            password_special_chars: bool = True,
            password_digits: bool = True,
            password_upper_case: bool = True,
            password_lower_case: bool = True,
            domains: List,
            latter_from_email: bool =True,
    ) -> UserFields:
        full_email = cls._faker.email()
        username = full_email.split("@")[0]
        domain = full_email.split("@")[1].split(".")[0]
        domain_zone = random.choice(domains)
        email_for_password = full_email if latter_from_email else None
        password = cls._generate_password(
            length=password_length,
            special_chars=password_special_chars,
            digits=password_digits,
            upper_case=password_upper_case,
            lower_case=password_lower_case,
            text=email_for_password,
        )

        return UserFields(
            email=username,
            password=password,
            domain=domain,
            domain_zone=domain_zone
        )
