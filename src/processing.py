from typing import Union


def filter_by_state(new_dict: Union[list]) -> Union[list]:
    clear_new_dict = []
    for i in new_dict:
        if i['state'] == 'EXECUTED':
            clear_new_dict.append(i)
    return clear_new_dict


