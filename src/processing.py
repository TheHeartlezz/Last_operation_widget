def filter_by_state(banking_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключ
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state  соответствует указанному значению"""
    banking_filter: list[dict] = []  # отфильтрованный список словарей
    for banking in banking_list:
        if banking["state"] == state:
            banking_filter.append(banking)
    return banking_filter


def sort_by_date(banking_list: list[dict], is_reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр direction,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате"""
    banking_sorted = sorted(banking_list, key=lambda banking: banking["date"], reverse=is_reverse)
    return banking_sorted
