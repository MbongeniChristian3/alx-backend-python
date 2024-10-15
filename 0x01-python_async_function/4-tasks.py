#!/usr/bin/env python3
'''Spawns task_wait_random n times with the specified max_delay and
returns the list of all delays in ascending order

    Parameters:
    n (int): The number of times to spawn task_wait_random.
    max_delay (int): The maximum delay in seconds.

    Returns:
    List[float]: The list of delays in ascending order.
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
