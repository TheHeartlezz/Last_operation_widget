def get_mask_card_number(card_number: int) -> str:
    """Функция в качестве аругента получает номер карты клиента как целое число и возвращет
    его в виде маскированной строки"""

    masked_card_number = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-5:-1]
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """Функция в качестве аругента получает номер счета клиента как целое число и возвращет
    его в виде маскированной строки"""

    masked_account_number = "**" + str(account_number)[-5:-1]
    return masked_account_number
