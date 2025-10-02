"""
A module that adds numbers together.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""


def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """
    Subtracts two numbers and computes `a` minus `b`.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        A second number to be subtracted from `a`.

    Returns
    -------
    float
        The difference of the two numbers.

    Examples
    --------
    >>> subtract_numbers(5, 3)
    2
    >>> subtract_numbers(-2, 7)
    -9
    """
    return a - b


def add_list_of_numbers(numbers: list) -> float:
    """
    Add a list of numbers together.

    Returns 0 if `numbers` is empty.

    Parameters
    ----------
    numbers : List of floats to be added.

    Returns
    -------
    float
        The sum of the values in the list.

    Examples
    --------
    >>> add_list_of_numbers([1, 2, 3])
    3
    >>> add_list_of_numbers([])
    0
    >>> add_list_of_numbers([1])
    1
    """
    result = 0
    for a in numbers:
        result = add_numbers(result, a)
    return result