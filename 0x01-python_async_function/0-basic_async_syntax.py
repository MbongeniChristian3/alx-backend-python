#!/usr/bin/env python3
'''Waits for a random delay between 0 and max_delay (inclusive) seconds and returns the delay.

    Parameters:
    max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    Union[int, float]: The actual delay in seconds.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
