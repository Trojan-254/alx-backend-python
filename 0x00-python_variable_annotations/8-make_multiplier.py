#!/usr/bin/env python3
"""module for type-annotated function make_multiplier"""
import typing
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
   """takes a float as arg
   returns a function that mulitiplies
   a float by multioplier"""

   def multiply(number: float) -> float:
      return number * multiplier
   return multiply

