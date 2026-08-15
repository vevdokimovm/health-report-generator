from src.entities.report import Report
from src.infra.db.common.models import ID


async def get_report(
        report_id: ID,
        db_gateway: ...
) -> Report:
        """
        Получение отчета по уникальному идентификатору.

        :param report_id: Идентификатор отчёта
        :param db_gateway: Шлюз к внутренней базе данных
        :return: Полученный отчёт
        """