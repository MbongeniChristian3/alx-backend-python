#!/usr/bin/env python3
import asyncio
import random
import time
from typing import List


async def wait_random(max_delay: int) -> float:
    '''Asynchronous coroutine that waits for a random delay between 0 and max_delay.'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns wait_random n times with the given max_delay and returns a list of delays in ascending order.'''
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insert delays in ascending order
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)  # Append at the end if it's the largest
    return delays


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the total execution time for wait_n and returns the average time per execution.'''
    start_time = time.time()  # Start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.time()  # End time
    total_time = end_time - start_time  # Total elapsed time
    return total_time / n  # Return the average time per execution
