#!/usr/bin/python3
"""Task 4 module"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False."""
    return (type(obj) is not a_class and isinstance(obj, a_class))
