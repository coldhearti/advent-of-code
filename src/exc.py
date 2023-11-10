from typing import Any, Callable


class NotImplementedError(Exception):
    ...


class UnderConstructionError(Exception):
    ...


def under_construction(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def exc_wrap(*args: Any, **kwargs: Any):
        func(*args, **kwargs)
        raise UnderConstructionError(func.__module__.split(".")[1] + "." + func.__name__)

    return exc_wrap


def not_implemented(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def exc_wrap(*args: Any, **kwargs: Any):
        func(*args, **kwargs)
        raise NotImplementedError(func.__module__.split(".")[1] + "." + func.__name__)

    return exc_wrap
