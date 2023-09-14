#!/usr/bin/python3
def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)