#in the name of GOD
#SeyyedMahdiHassanpour
#smahdi1991@gmail.com
"""
lottery algorithm
this algorithm can be use in banking lottery
each one has its own ...

"""
import random
from collections import defaultdict
scores = list(range(1, 500, 5))
#print(scores)


def lottery1():
    fair_list = [score for score in scores for _ in range(score)]
    #print(fair_list)
    return random.choice(fair_list)

#print(lottery1())

d = defaultdict(int)  # we will see each score selection count
for _ in range(10000):
    d[lottery1()] += 1

print(sorted(d.items()))
# from pprint import pprint as pp
# import random
# import collections
# import math
# min_score = 0
# max_score = 501
# multiple = 25
#
# scores = range(min_score, max_score, multiple)
# candidate = [scores.index(s) for s in scores for _ in range(s)]
# benchmarks = dict.fromkeys(candidate, 0)
#
# for _ in range(100000):
#     benchmarks[random.choice(candidate)] += 1
# print(collections.OrderedDict(sorted(benchmarks.items())))
#
#
# def f():
#     c = math.ceil(math.pow(random.random(), .5) * max(candidate))
#     return c
#
# benchmarks = dict.fromkeys(candidate, 0)
# for _ in range(100000):
#     benchmarks[f()] += 1
# print(collections.OrderedDict(sorted(benchmarks.items())))
