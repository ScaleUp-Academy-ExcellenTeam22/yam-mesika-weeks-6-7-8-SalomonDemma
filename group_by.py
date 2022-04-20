
def group_by(func: callable, data_base: iter) -> dict:
    """
    This function create a dictionary of groups. the key is by the function received and the item is
    a list of the values that have the same value return by the function.
    :param func: a function that that will group value
    :param data_base: an iterable data base that the function will read value from
    :return: dictionary of grouped value
    """
    dic = dict()
    for fun_key in data_base:
        dic.setdefault(func(fun_key), list()).append(fun_key)
    return dic


if __name__ == "__main__":
    lst = ["hi", "bye", "yo", "try"]
    print(group_by(len, lst))
