#!/usr/bin/env python3
"""module for type-annotated function sum_mixed_list"""
import typing
from typing import List, Union


def sum_mixed_list(mxd_list: list[Union[int, float]]) -> float:
    """takes a list of integers and floats
    returns their sum as a float"""

    return sum(mxd_list)
