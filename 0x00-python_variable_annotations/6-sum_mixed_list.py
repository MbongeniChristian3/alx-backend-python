#!/usr/bin/env python3
"""
This module provides a function to compute the sum of
a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]])

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return float(sum(mxd_lst))
