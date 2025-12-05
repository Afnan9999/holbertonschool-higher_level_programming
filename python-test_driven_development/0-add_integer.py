#!/usr/bin/python3
"""
This module defines a function that safely adds two numeric values.
It ensures both arguments are integers or floats containing finite
numeric values. Floats are cast to integers before addition. The
function returns the integer result of the sum of the validated
arguments.
"""


def add_integer(a, b=98):
    """
    Add two integers after validating both inputs.

    This function checks that each argument is an integer or float,
    rejects NaN and infinite values, casts floats to integers, and
    returns the sum as an integer.
    """
    for value, name in ((a, "a"), (b, "b")):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be an integer")

        # Reject NaN and infinities to avoid ValueError or OverflowError
        if isinstance(value, float):
            if value != value:     # NaN check
                raise TypeError(f"{name} must be an integer")
            if value in (float('inf'), float('-inf')):
                raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)

