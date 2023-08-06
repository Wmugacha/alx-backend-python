#!/usr/bin/env python3
"""
Add correct duck type annotations
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Add annotations"""
    if lst:
        return lst[0]
    else:
        return None
