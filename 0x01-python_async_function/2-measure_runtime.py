#!/usr/bin/env python3
"""
Mutiple Coroutines
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Multiple Coroutines"""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    exec_time = (end - start) / n

    return exec_time
