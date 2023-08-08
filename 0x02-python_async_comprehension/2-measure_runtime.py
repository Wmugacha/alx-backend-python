#!/usr/bin/env python3
"""
Module to measure runtime of function
"""
import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine to call another"""
    start = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end = time.time()

    exec_time = (end - start)

    return exec_time
