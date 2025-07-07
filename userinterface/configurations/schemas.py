from pydantic import BaseModel


class UserFields(BaseModel):
    password: str
    email: str
    domain: str
    domain_zone: str
