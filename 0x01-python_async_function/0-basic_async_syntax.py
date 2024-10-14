#!/usr/bin/env python3

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds."""
    delay = uniform(0, max_delay)  # Get random float between 0 and max_delay
    await asyncio.sleep(delay)  # Asynchronously wait for that time
    return delay
