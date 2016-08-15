import time
# def my_range(*args):
#     start, stop, step = 0, 10, 1
#     if len(args) == 3:
#         start, stop, step = args
#     elif len(args) == 2:
#         start, stop = args
#     elif len(args) == 1:
#         stop = args[0]
#     else:
#         print("DOROST nashod")
#         return -1
#     while start < stop:
#         yield start
#         start += step

# for i in my_range(1, 10, 2):
#     print(i)
# g = my_range(5)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def d(f):
    def fn(a):
        # print("MR. ")
        print(f.__name__)
        f(a)
        # print('. ')
    return fn


@d
def get_name(age):
    print("ALI KALAN")
    print(age)

# get_name(10)


# def h():
#     def g():
#         print("G")
#     return g
#
# h()()

# def alaki(a, b):
#     """
#     :param a
#     """
#     a = 10 + b
#     return a


def memo(f):
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            result = cache[args] = f(*args)
            return result
        except TypeError:
            return f(*args)
    return _f


@memo
def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n - 1) + fib(n - 2)

# t0 = time.clock()
# fib(35)
# print("%5.15f" % (time.clock() - t0))


# s = "SELECT {name} FROM users WHERE id > {id}".format(name='email', id=10)
# s = "SELECT {0} FROM users WHERE id > {1}".format('email', 10)
# s = "SELECT %s FROM users WHERE id > %s" % ('email', 10)
# print(s)

import collections

words = "THIS IS SOME STRING !! and A Ali kalan".split()
d = collections.defaultdict(list)
for w in words:
    d[len(w)].append(w)

d_order = collections.OrderedDict(d.items())
print([v for mv in d_order.values() for v in mv])







