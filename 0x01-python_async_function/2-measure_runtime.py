#!/usr/bin/env python3
import asyncio
import random
import time
from typing import List


async def wait_random(max_delay: int) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return delays


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
