#!/usr/bin/env python3
"""module for element_length type-annotated function"""
import typing
from typing import Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """returns values with appropriate types"""
    return [(i, len(i)) for i in lst]
