#!/usr/bin/env python3
"""module for typed-annotated function sum_list"""
import typing
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats as args
    returns their sum as a float"""

    return sum(input_list)
