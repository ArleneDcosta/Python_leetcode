cache = {}
#https://medium.com/coders-mojo/complete-system-design-series-part-1-45bf9c8654bc
def cached_func(func):
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cached_func
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

