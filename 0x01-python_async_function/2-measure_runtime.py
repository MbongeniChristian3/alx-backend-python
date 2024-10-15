#!/usr/bin/env python3
''' Measures the total execution time for wait_n(n, max_delay)
and returns the average time per call.

    Parameters:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay in seconds.

    Returns:
    float: The average time per call.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
