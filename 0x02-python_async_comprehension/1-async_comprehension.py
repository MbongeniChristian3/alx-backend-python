#!/usr/bin/env python3
''' Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.

 Parameters:
    max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    return the 10 random numbers.

'''
import asyncio
import random


async def async_generator():
    """Yield 10 random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()


async def async_comprehension():
    """Collect 10 random numbers from async_generator using async comprehension."""
    return [i async for i in async_generator()]


async def main():
    result = await async_comprehension()
    print(result)


asyncio.run(main())
