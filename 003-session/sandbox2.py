# a, b = 1, 1
# for _ in range(100):
#     print(a)
#     a, b = b, a + b


# def memo(f):
#     cache = {}
#
#     def _f(*args):
#         try:
#             return cache[args]
#         except KeyError:
#             result = cache[args] = f(*args)
#             return result
#         except TypeError:
#             return f(*args)
#     return _f
#
#
# @memo
# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(40))