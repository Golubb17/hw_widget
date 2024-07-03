from typing import Any


def filter_by_state(new_list: list[dict[str:Any]], state_id: str = 'EXECUTED') -> Any:
    """Функция проверяет словари в списке на статус 'state', и оставляет значения только со статусом 'EXECUTED'"""
    clear_new_list = []
    for i in new_list:
        if i['state'] == state_id:
            clear_new_list.append(i)
    return clear_new_list


def sort_by_date(date_list: list[dict[str:Any]], reverse: bool = True) -> Any:
    """Функция сортирует список словарей по дате"""
    sorted_list_date = sorted(date_list, key=lambda date_list: date_list['date'], reverse=reverse)
    return sorted_list_date
