from datetime import time

from pydantic import BaseModel


class UserFields(BaseModel):
    password: str
    email: str
    domain: str
    domain_zone: str


class TestData(BaseModel):
    interest_selection_count: int
    timer_start: time
