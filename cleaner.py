def filter_nondigits(data: list) -> list:
    """
    Processes heart rate datasets, removes new line characters, and filters out non-numeric data 
    that is invalid or missing

    Args:
        data (list[string]): list of string that contains heart rate dataset

    Returns:
        list[int]: list of integer that represent the valid heart rate dataset 
    """
    result = []
    for val in data:
        val = val.strip()
        if val.isdigit():
            result.append(int(val))
    return result
