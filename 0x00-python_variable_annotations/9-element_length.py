#!/usr/bin/env python3
"""
Add annotations
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function to iterate a tuple"""

    return [(i, len(i)) for i in lst]
