#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number.

    Args:
        number (int): The number whose last digit is to be printed.

    Returns:
        The last digit of the number.
    """
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return last_digit

if __name__ == "__main__":
    # Your test code here
    pass
