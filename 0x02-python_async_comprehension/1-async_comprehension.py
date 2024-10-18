#!/usr/bin/env python3
"""module for coroutine async_comprehension"""
import random
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """takes no args
    returns ten random numbers"""
    return [num async for num in async_generator()]
