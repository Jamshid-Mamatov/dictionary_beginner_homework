def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """

    list_int=[]
    for i in data.keys():
        if str(i).isdigit():
            list_int.append(i)

    return list_int
