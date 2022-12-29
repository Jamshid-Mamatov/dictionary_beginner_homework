def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    list_user=[]
    for i  in data:
        if i['age']==age:
            list_user.append(i['name'])
    return list_user
