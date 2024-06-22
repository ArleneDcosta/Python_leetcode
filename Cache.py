import functools

def cache(func):
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cached_results:
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]

    return wrapper

@cache
def expensive_function(n):
    print("Calculating...")
    return n * n

# First call - the result will be calculated and cached
print(expensive_function(5))

# Second call with the same argument - the result will be fetched from the cache
print(expensive_function(5))

# Another call with a different argument - the result will be calculated and cached separately
print(expensive_function(10))
