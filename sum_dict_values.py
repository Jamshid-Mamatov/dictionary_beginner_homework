def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    sum_leng_val=0
    for i in data.values():
        sum_leng_val+=i
    return sum_leng_val