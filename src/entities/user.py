from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class User:
    id: int
    name: str
    email: str
    date_of_birth: date