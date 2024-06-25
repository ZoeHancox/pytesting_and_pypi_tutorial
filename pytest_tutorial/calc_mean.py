def calculate_mean(numbers):
    """
    Calculate the mean of a list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        float or None: The mean of the numbers in the list.
                       Returns None if the list is empty.

    Example:
        >>> numbers = [1, 2, 3, 4, 5]
        >>> calculate_mean(numbers)
        3.0
    """

    if len(numbers) == 0:
        return None
    else:
        return sum(numbers) / len(numbers)