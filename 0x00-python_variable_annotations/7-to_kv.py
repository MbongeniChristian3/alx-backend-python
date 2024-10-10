#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string and a number.

"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple containing a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k
        and the second element is the square of v.
    """
    return (k, float(v ** 2))


