#!/usr/bin/python3
"""
Module to calculate minimum number of operations to achieve n H characters
"""


def minOperations(n):
    """Calculate the fewest number of operations for n H characters.

    Args:
        n (int): The desired number of H characters

    Returns:
        int: Minimum number of operations needed, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while i <= n:
        while n % i == 0:
            operations += i
            n = n // i
        i += 1

    return operations
