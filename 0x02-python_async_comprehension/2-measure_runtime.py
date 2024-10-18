#!/usr/bin/env python3
"""module for  coroutine measure_runtime"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measures the total runtime and returns it"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_runtime = time.time() - start_time
    return total_runtime
