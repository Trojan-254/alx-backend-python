#!/usr/bin/env python3
"""module for safely_get_value function"""
import typing
from typing import Mapping, Any, Union

def safely_get_value(dct: Mapping, key: Any, default: Union[~T, None]) -> Union[Any, ~T]:
    if key in dct:
        return dct[key]
    else:
        return default
