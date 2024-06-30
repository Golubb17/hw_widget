import masks
from typing import Union


def mask_account_card(value: Union[str]) -> Union[str]:
    """Функция получает строку с данными счета или карты и выводит их маску"""
    n_list = value.split()
    words = []
    numbers = []
    for i in n_list:
        if not i.isdigit():
            words.append(i)
        else:
            numbers.append(i)
    if "Счет" in words:
        answer = "Счет " + masks.mask_account(numbers[0])
        return answer
    else:
        answer = ' '.join(words) + " " + masks.mask_card(numbers[0])
        return answer

def get_data(data: Union[str]) -> Union[str]:
    """Функция принимает дату и выводит ее в корректом виде"""
    return data[:4] + "." + data[5:7] + "." + data[8:10]
