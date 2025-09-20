def fibonacci_series(n_terms):
    """
    Generates and prints the Fibonacci series up to a specified number of terms.

    Args:
        n_terms (int): The number of terms to generate in the Fibonacci series.
    """
    if n_terms <= 0:
        print("Please enter a positive integer for the number of terms.")
        return
    elif n_terms == 1:
        print("Fibonacci series:")
        print(0)
        return

    a, b = 0, 1
    count = 0
    print("Fibonacci series:")
    while count < n_terms:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1
    print()  # For a new line after the series

# Example usage:
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacci_series(num_terms)
