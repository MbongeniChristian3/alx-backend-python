#!/usr/bin/env python3

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of the sequence if available, else None.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Optional[Any]: The first element of the sequence, or None
    """
    if lst:
        return lst[0]
    else:
        return None
