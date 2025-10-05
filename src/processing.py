def filter_by_state(transaction_log: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключ
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state  соответствует указанному значению"""
    transaction_filter = []  # отфильтрованный список словарей
    for transaction_item in transaction_log:
        if transaction_item["state"] == state:
            transaction_filter.append(transaction_item)
    return transaction_filter


def sort_by_date(transaction_log: list, is_reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр direction,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате"""
    transaction_sorted = sorted(transaction_log, key=lambda transaction: transaction["date"], reverse=is_reverse)
    return transaction_sorted
