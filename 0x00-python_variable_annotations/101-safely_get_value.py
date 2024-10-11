from typing import Any, TypeVar, Dict, Optional

T = TypeVar('T')  # Declare a TypeVar to represent the type of the default


def safely_get_value(
    dct: Dict[Any, T], key: Any, default: Optional[T] = None
) -> Optional[T]:
    """Safely gets a value from a dictionary.

    Args:
        dct (Dict[Any, T]): A dictionary where keys are of any type and values
        are of type T.
        key (Any): The key used to retrieve a value from the dictionary.
        default (Optional[T], optional): The default value to return if the
        key is not found. Defaults to None.

    Returns:
        Optional[T]: The value from the dictionary associated with the key,
        or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
