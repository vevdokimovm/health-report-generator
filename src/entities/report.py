from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Report:
    user_id: int
    status: str
    storage_path: Path
    error_details: str | None = None
    send_weekly: bool = False
    send_monthly: bool = False
