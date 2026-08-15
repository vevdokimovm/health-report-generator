from src.entities.report import Report


async def change_report(
        new_report: Report,
        db_gateway: ...,
) -> Report:
    """
    Изменение данных в отчёте

    :param new_report: Отчет с внесёнными изменениями
    :param db_gateway: Шлюз к внутренней базе данных

    :return: Изменённый отчёт
    """