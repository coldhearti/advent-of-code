from typing import Callable


class NotImplementedError(Exception):
    ...


class UnderConstructionError(Exception):
    ...


def under_construction(func: Callable):
    def exc_wrap(*args, **kwargs):
        func(*args, **kwargs)
        raise UnderConstructionError(func.__module__.split(".")[1] + "." + func.__name__)

    return exc_wrap


def not_implemented(func: Callable):
    def exc_wrap(*args, **kwargs):
        func(*args, **kwargs)
        raise NotImplementedError(func.__module__.split(".")[1] + "." + func.__name__)

    return exc_wrap
