def get_user_names(data:list, country:str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    list_user=[]
    for i  in data:
        if i['country']==country:
            list_user.append(i['name'])
    return list_user