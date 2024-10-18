#!/usr/bin/env python3
"""module for coroutine async_generator"""
import random
import asyncio


async def async_generator() -> float:
    """takes no arguments
    yields a random number between 0 and 10"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
