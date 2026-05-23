from functools import wraps


def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):

        key = str(args) + str(kwargs)

        if key in cache:
            print("Cache hit")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result

        return result

    return wrapper
