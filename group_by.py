
from collections.abc import Iterable
from typing import Optional


def group_by(func: Optional[callable], iterable: Iterable) -> dict:
    """
    This function creates a dictionary of groups. The key is by the function received and the item is
    a list of the values that have the same value return by the function.
    :param func: A function that that will group value
    :param iterable: An iterable that the function will read value from
    :return: Dictionary of grouped value
    """
    dictionary_group = dict()
    for fun_key in iterable:
        dictionary_group.setdefault(func(fun_key), list()).append(fun_key)
    return dictionary_group


if __name__ == "__main__":
    lst = ["hi", "bye", "yo", "try"]
    print(group_by(len, lst))
