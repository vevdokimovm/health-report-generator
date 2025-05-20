from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class EmailLog:
    id: int
    report_id: int
    receiver_id: int
    send_at: datetime
    status: str
    error_details: str | None = None
