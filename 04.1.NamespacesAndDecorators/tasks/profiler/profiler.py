import time
from functools import wraps

def profiler(func):  # type: ignore
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start_time = time.time()
        result = func(*args, **kwargs)
        wrapper.last_time_taken = time.time() - start_time
        return result

    wrapper.calls = 0
    wrapper.last_time_taken = 0.0
    return wrapper
