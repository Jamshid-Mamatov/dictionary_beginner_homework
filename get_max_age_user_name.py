def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    max=0
    name=""
    for i in data:
        if max<i['age']:
            name=i['name']
            max=i['age']
    return name