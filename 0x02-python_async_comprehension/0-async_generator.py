#!/usr/bin/env python3
'''
loops 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10.

 Parameters:
    takes no arguments.

  Returns:
    Union[int, float]: Random delay between 0 and 10.
'''

import random
import asyncio


async def async_generator():
    """Asynchronously yield a random float between 0 and 10, ten times."""
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)
