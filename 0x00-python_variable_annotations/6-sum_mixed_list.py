#!/usr/bin/env python3
"""
Module that returns the sum of a list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """Function that returns the sum of floats in a list"""

    return sum(mxd_list)
