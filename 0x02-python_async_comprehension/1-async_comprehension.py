#!/usr/bin/env python3
import asyncio
import random


# Define the async_generator function to yield random numbers
async def async_generator():
    """Yield 10 random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)  # Simulate an async operation
        yield random.random()  # Yield a random float between 0 and 1


# Define async_comprehension
async def async_comprehension():
    """Collect 10 random numbers from async_generator using async comprehension."""
    return [i async for i in async_generator()]


# Example of using the async_comprehension
async def main():
    result = await async_comprehension()
    print(result)

# Run the main function
asyncio.run(main())
