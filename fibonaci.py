# fibonaci 100
# a = b = 1
# count = 0
# print(a)
# print(b)
# while count < 300:
#    a, b = b, a+b
#    print(b)
#    count += 1
# pythonic with dummy variable name _


def dynamic_fib(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


# add memorization(cache) to recursive fib:
cache_dict = dict()


def fib_recursive_memorization(n):
    # LBYL approach
    # if n in cache_dict:
    #   return cache_dict[n]
    # EAFP approach is much better and faster approach in developing
    try:
        value = cache_dict[n]
        return value
    except KeyError:
        if n == 1 or n == 0:
            return 1
        cache_dict[n] = fib_recursive_memorization(n - 1) + fib_recursive_memorization(n - 2)
        return cache_dict[n]

# @@@@@@@@@@@@@@@with better algorithm we get performance for free@@@@@@@@@@@@@
# simple recursive fib has a limit at 35 to quickly answer, but we use a decorator for it
def decorator_cache_extend_simple_fib(fib_simple):
    cache = {}

    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = fib_simple(*args)
            return result
        except TypeError:
            return -1#fib_simple(*args)

    return wrapper


@decorator_cache_extend_simple_fib
def fib_recursive_simple(n):
    if n <= 1:
        return 1
    return fib_recursive_simple(n - 1) + fib_recursive_simple(n - 2)


print(dynamic_fib(36))
print(fib_recursive_simple(36))
print(fib_recursive_memorization(36))


# import matplotlib.pyplot as plt
# X = range(100)
# Y = [2**n for n in X]
# plt.plot(X, Y)
# plt.show()
