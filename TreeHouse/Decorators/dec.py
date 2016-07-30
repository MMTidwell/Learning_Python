from __future__ import print_function
from functools import wraps

# Decorators are clean, small, and easy to remove. These are good for longer functions that hold sums/totals
#   Are functions that accept functions as arguments. They have inner functions that preforms some actions before
#   returning the accepted function. the outer function really returns the inner function. The inner function really
#   doesnt have to return the unction that was passed in.
# You can nest functions inside of other functions.
# CLOSER- predefined function that has a scope


def outer():
    # scope
    number = 5

    def inner():
        print(number)

    # always has access to number variable
    inner()


# returns the output of func when supplied x and y
def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


# passing a function into another function
# print(function name(using function name, arg, arg))
print(apply(add, 5, 5))
print(apply(sub, 2, 8))


def close():
    x = 20

    def inner():
        print(x)
    return inner()


# calls close() and return inner
closure = close()
closure


def add_to_five(num):
    def inner():
        print(num+5)
    return inner

fifteen = add_to_five(10)
fifteen()


def log_me(func):
    # We imported logging here since we want it to be available but we don't want to have to use logging just to
    #   import the decorator.
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        # args and kwargs do not have the * in front of them, we want the tuple and the dic
        logging.debug("Called {} with args {} and kwargs {}.".format(func.__name__, args, kwargs))
        # we use the * in from of args and kwargs, because we are calling on them
        return func(*args, **kwargs)
    return inner


@log_me
def sub(x, y):
    """Returns the diff between 2 numbers"""
    return x - y


"""
>>> sys.path.extend(['C:\\Users\\mittsy\\Google Drive\\PROGRAMMING\\PYTHON\\TreeHouse\\decorators'])
>>> from dec import log_me
10
-6
20
15
>>> def print_2():
...     print(2)
...
>>> print_2()
2
>>> print_2 = log_me(print_2)
>>> print_2()
DEBUG:root:Called print_2.
2

>>> @ log_me
... def print_4():
...     print(4)
...
>>> print_4()
DEBUG:root:Called print_4.
4
"""

"""
>>> sys.path.extend(['C:\\Users\\mittsy\\Google Drive\\PROGRAMMING\\PYTHON\\TreeHouse\\decorators'])
>>> from dec import log_me
10
-6
20
15
>>> @log_me
... def sub(x, y, switch=False):
...     return x - y if not switch else y - x
...
>>> sub(5, 2)
DEBUG:root:Called sub with args (5, 2) and kwargs {}.
3
>>> sub(5, 2, switch=True)
DEBUG:root:Called sub with args (5, 2) and kwargs {'switch': True}.
-3
"""

"""
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)] on win32
>>> sys.path.extend(['C:\\Users\\mittsy\\Google Drive\\PROGRAMMING\\PYTHON\\TreeHouse\\decorators'])
>>> from dec import sub
10
-6
20
15
>>> sub.__name__
'sub'
>>> help(sub)
Help on function sub in module dec:

sub(*args, **kwargs)
    Returns the diff between 2 numbers

>>> sub(5, 2)
3
DEBUG:root:Called sub with args (5, 2) and kwargs {}.
"""