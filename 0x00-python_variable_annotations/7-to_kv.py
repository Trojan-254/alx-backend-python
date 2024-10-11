#!/usr/bin/env python3
"""module for annotated-function to_kv"""
import typing
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a str, int or float as args
    returns a tuple"""

    return k, v * v
