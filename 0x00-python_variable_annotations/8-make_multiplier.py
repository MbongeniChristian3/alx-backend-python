#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the multiplier.

    Args:
        multiplier (float): The multiplier to be used in the multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """Multiplies the given value by the multiplier."""
        return value * multiplier
    
    return multiplier_function


