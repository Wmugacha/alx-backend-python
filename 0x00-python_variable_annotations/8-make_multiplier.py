#!/usr/bin/env python3
"""
Module that returns a multiplacation
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that call another"""

    def factor(x: float) -> float:
        """Function that multiplies two floats"""

        return x * multiplier
    return factor
