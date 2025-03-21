def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
        list: a empty list if input data(list) is empty
    """
    if not data:
        return []

    total = 0
    for val in data:
        total += val
    total = total/len(data)

    return round(total,2)


def maximum(data: list) -> float:
    """
    Find out the maximum heart rate by iterating through the list

    Args:
        data (list[int]): list of integers representing heart rate samples

    Returns:
        int: a integer value representing the maximum heart rate of this list
        list: a empty list if input data(list) is empty
    """
    if not data:
        return []

    max_val = -1
    for val in data:
        if val > max_val:
            max_val = val

    return max_val


def variance(data: list) -> float:
    """
    Calculate population variance

    Args:
        data (list[int]): list of integers representing heart rate samples

    Returns:
        float: a floating point value representing the variance of this list
    """
    if not data:
        return 0

    avg = average(data)
    result = 0
    for val in data:
        result += (val-avg)**2

    result = result/len(data)
    return round(result,2)


def standard_deviation(data: list) -> float:
    """
    Calculate population standard deviation

    Args:
        data (list[int]): list of integers representing heart rate samples

    Returns:
        float: a floating point value representing the standard deviation of this list
        list: a empty list if input data(list) is empty
    """
    if not data:
        return []

    result = variance(data)**0.5

    return round(result,2)
