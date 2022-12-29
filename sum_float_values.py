def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    sum_float=0
    for value in data.values():

        if int(value)!=value:
            sum_float+=value


    return sum_float
