from collections.abc import Callable 
from typing import Any, TypeVar
from collections import OrderedDict


Function = TypeVar('Function', bound=Callable[..., Any])


def cache(max_size: int) -> Callable[[Function], Function]:
    def decorator(function):
        cache = OrderedDict()

        def wrapper(*args):
            if args in cache:
                return cache[args]
            result = function(*args)
            if len(cache) >= max_size:
                cache.popitem(last=False)
            cache[args] = result
            return result

        return wrapper

    return decorator