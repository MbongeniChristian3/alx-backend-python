#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a float.

The purpose of this module is to demonstrate the use of type annotations
and provide a simple mathematical operation.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    Args:
        n (float): The float number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)


