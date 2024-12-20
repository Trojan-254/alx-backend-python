#!/usr/bin/env python3
"""module for type-annotated function safe_first_element"""
import typing
from typing import Sequence, Any, Union

# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
