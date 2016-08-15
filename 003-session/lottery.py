from pprint import pprint as pp
import random
import collections
import math
min_score = 0
max_score = 501
multiple = 25

scores = range(min_score, max_score, multiple)
candidate = [scores.index(s) for s in scores for _ in range(s)]
benchmarks = dict.fromkeys(candidate, 0)

for _ in range(100000):
    benchmarks[random.choice(candidate)] += 1
print(collections.OrderedDict(sorted(benchmarks.items())))


def f():
    c = math.ceil(math.pow(random.random(), .5) * max(candidate))
    return c

benchmarks = dict.fromkeys(candidate, 0)
for _ in range(100000):
    benchmarks[f()] += 1
print(collections.OrderedDict(sorted(benchmarks.items())))
