from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(slots=True)
class ChronicCondition:
    id: int
    title: str
    description: str

@dataclass(slots=True)
class HealthData:
    user_id: int
    sleep_hours: float
    stress_level: int
    activity_level: int
    chronic_conditions: Iterable[ChronicCondition]