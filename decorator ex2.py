import functools


def is_multiple(x):
    def real_decorator(func):
        # @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print("{0} indicates {1}'s multiple.".format(func.__name__, x))
            else:
                print("{0} does not indicate {1}'s multiple.".format(func.__name__, x))
            return r
        return wrapper
    return real_decorator

@is_multiple(3)
@is_multiple(7)
@is_multiple(10)
def add(a, b):
    return a + b

print(add(10, 20))
