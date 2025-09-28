from .mask import get_mask_account, get_mask_card_number


def mask_account_card(bank_card: str) -> str:
    """Принимать один аргумент — строку, содержащую тип и номер карты или счета
    и возвращмет максированную строку"""
    accesory_name = ''  # название входных данных
    accesory_number = ''  # номер входных данных
    for symbol in bank_card:
        if symbol.isalpha():
            accesory_name += symbol
        elif symbol.isdigit():
            accesory_number += symbol
    if accesory_name == 'Счет':
        masked_digit = get_mask_account(accesory_number)
    else:
        masked_digit = get_mask_card_number(accesory_number)
    return f'{accesory_name}: {masked_digit}'


def get_date(raw_date: str) -> str:
    """Функция изменяет форматы дата/время с машинного на человеческую дату
    в формате DD.MM.YYYY"""
    human_date = f'{raw_date[8:10]}.{raw_date[5:7]}.{raw_date[:4]}'
    return human_date
