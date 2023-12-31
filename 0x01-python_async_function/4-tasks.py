#!/usr/bin/env python3
"""
Module to run Wait_random n times
"""
from typing import List
from heapq import nsmallest
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async function to run wait_random n times"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)

    return nsmallest(n, results)
