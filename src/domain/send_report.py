from src.domain.common.models import EmailLog
from src.entities.report import Report


async def send_report(
        report: Report,
        db_gateway: ...,
        email_gateway:...,
    ) -> EmailLog: ...