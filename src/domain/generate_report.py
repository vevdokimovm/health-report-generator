from src.entities.report import Report


async def generate_report(
        api_gateway: ...,
        db_gateway: ...,
) -> Report:
    """
    Создание нового отчёта

    :param api_gateway: Шлюз API внутренних сервисов
    :param db_gateway: Шлюз внутренней базы данных

    :return: Готовый отчёт
    """