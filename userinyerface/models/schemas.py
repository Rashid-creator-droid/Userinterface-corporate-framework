from datetime import time
from typing import Dict

from pydantic import BaseModel


class UserFields(BaseModel):
    password: str
    email: str
    domain: str
    domain_zone: str


class LanguageDialogConfig(BaseModel):
    dialog_title: str
    edit: str
    open_button: str


class DataTest(BaseModel):
    interest_selection_count: int
    timer_start: time
    os_language: Dict[str, LanguageDialogConfig]
