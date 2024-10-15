#!/usr/bin/env python3
"""module for coroutine function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes an int arg, waits for random delay
    returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
