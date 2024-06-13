from typing import Union


def mask_card(number_card: Union[str]) -> Union[str]:
    """Функция, которая превращает номер карты - в маску номера карты"""
    masked_card = number_card[:4] + " " + number_card[4:6] + "**" + " " + "****" + " " + number_card[12:]
    return masked_card


def mask_account(number_account: Union[str]) -> Union[str]:
    """Функция, которая превращает номер счета - в маску номера счета"""
    masked_account = "**" + number_account[16:]
    return masked_account
