#!/usr/bin/env python3
'''Creates and returns an asyncio.Task for the coroutine wait_random
with the given ma>

    Parameters:
    max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    asyncio.Task: The created asyncio.Task for wait_random.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asynchronous task for wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))
