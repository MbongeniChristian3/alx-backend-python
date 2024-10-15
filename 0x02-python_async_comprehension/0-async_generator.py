#!/usr/bin/env python3
'''
task 0 module
'''

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously yield a random float between 0 and 10, ten times."""
    for _ in range(10):
        await asyncio.sleep(1)  
        yield random.random() * 10
