def fibonacci(num: int) -> int:
    """
    generates n element of fibonacci sequence
    :param num: integer
    :return: element (integer)

    """
    if num <= 0:
        raise ValueError("The element should be positive")

    if num == 1 or num == 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)
