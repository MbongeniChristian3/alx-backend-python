#!/usr/bin/env python3
import asyncio
from basic_async_syntax import wait_random  # Importing wait_random function


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates and returns an asyncio.Task that runs wait_random.'''
    return asyncio.create_task(wait_random(max_delay))  # Create and return the task
