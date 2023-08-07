#!/usr/bin/env python3
"""
Module to create async Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns an async task"""

    task1 = asyncio.create_task(wait_random())

    return task1
