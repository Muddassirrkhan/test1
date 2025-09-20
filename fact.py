def factorial_iterative(n):
    """
    Calculates the factorial of a non-negative integer using an iterative approach.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is a negative number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
number = 5
try:
    print(f"The factorial of {number} is {factorial_iterative(number)}")
except ValueError as e:
    print(e)

number_negative = -3
try:
    print(f"The factorial of {number_negative} is {factorial_iterative(number_negative)}")
except ValueError as e:
    print(e)
