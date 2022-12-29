def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    sum_leng_val=0
    for i in data.values():
        sum_leng_val+=len(i)
    return sum_leng_val