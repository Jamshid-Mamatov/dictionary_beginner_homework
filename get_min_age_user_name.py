def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    min=data[0]['age']
    name=data[0]['name']
    print(min,name)
    for i in data:
        if min>i['age']:
            name=i['name']
            min=i['age']
    return name
