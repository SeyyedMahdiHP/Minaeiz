import re
import time
import itertools

# a = [1, 3, -9, 4, 6,]
# print(sorted(a, key=lambda x : x ** 2))
# lambda O, D, E, V, N : O*10**0

# s = '1 + 2 == 3'
# if eval(s):
#     print("INJA")

# s1 = 'ABC'
# s2 = '123'
#
# table = str.maketrans(s1, s2)
# print('A + B == C + B + A - C'.translate(table))

# print(list(itertools.permutations("0987654321", 5)))

# m1 = re.match('a.i', 'kalan ali')
# m2 = re.search('a.i', 'kalan ali')
# print(m2.group())

# s = 'ODD + ODD == EVEN'
# print(re.findall('[A-Z]', s))
# print(re.split('(==)', s))


# s = 'ali'
# p = 'a'
#
#
# def n_w_1(p, s):
#     if p in s:
#         return True
#
#
# def re_w_1(p, s):
#     if re.search(p, s):
#         return True
#
# t0 = time.clock()
# for _ in range(10000):
#     n_w_1(p, s)
# print("{0:f}".format(time.clock() - t0))
# t0 = time.clock()
# for _ in range(10000):
#     re_w_1(p, s)
# print("{0:f}".format(time.clock() - t0))
# nw:   0.001901
# re_w: 0.011044

# s = 'ali'
# p = 'al+i'
#
#
# def re_w_2(s, p):
#     return re.search(p, s)
#
#
# def n_w_2(s, p):
#     if p[0] == s[0] and p[-1] == s[-1]:
#         for i in s[1:-1]:
#             if i != 'l':
#                 return False
#     else:
#         return False
#     return True
#
# t0 = time.clock()
# for _ in range(10000):
#     n_w_2(p, s)
# print("{0:f}".format(time.clock() - t0))
# t0 = time.clock()
# for _ in range(10000):
#     re_w_2(p, s)
# print("{0:f}".format(time.clock() - t0))
# 0.005970
# 0.009126

# print(re.search('ع.ی', 'علی'))





















