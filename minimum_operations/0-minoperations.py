#!/usr/bin/python3
"""
Module to calculate minimum number of operations to achieve n H characters
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve n H characters
    Args:
        n (int): The desired number of H characters
    Returns:
        int: Minimum number of operations needed, or 0 if impossible
    """
    # If n is 1 or less, no operations are needed
    if n <= 1:
        return 0

    # Initialize variables
    operations = 0
    i = 2

    # Find prime factors
    while i <= n:
        while n % i == 0:
            # Add the current prime factor to operations
            operations += i
            # Divide n by the prime factor
            n = n // i
        i += 1

    return operations
