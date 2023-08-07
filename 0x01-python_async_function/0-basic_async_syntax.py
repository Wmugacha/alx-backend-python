#!/usr/bin/env python3
"""
Module of an asynch function
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Function utilizing random module to
    initiate a delay"""
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
