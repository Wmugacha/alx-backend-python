#!/usr/bin/env python3
"""
Module to yield random numbers using a Coroutine
"""
from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine to yield 10 random numbers"""

    for _ in range(10):
        random_num = random.uniform(1, 10)

        await asyncio.sleep(1)

        yield random_num
