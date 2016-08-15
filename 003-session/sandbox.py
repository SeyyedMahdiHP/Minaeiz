import random
import itertools
import math
import collections

max_score = 501
min_score = 0
multiple = 25
scores = range(min_score, max_score, multiple)

# 1
candidates = [s for s in scores for _ in range(s)]
benchmarks = dict.fromkeys(scores, 0)
for _ in range(100000):
    benchmarks[random.choice(candidates)] += 1
print(collections.OrderedDict(sorted(benchmarks.items())))


# 2
acc = list(itertools.accumulate(scores))
max_s = max(acc)


def pick():
    r = random.randint(0, max_s)
    for i, v in enumerate(acc):
        if v >= r:
            return i


benchmarks = dict.fromkeys(scores, 0)
for _ in range(100000):
    benchmarks[scores[pick()]] += 1
print(collections.OrderedDict(sorted(benchmarks.items())))


# 3


def savvy_pick(num):
    c = math.floor(math.pow(random.random(), .5) * num)
    remainder = c % multiple
    if remainder == 0:
        return c
    return c + multiple - remainder


benchmarks = dict.fromkeys(scores, 0)
for _ in range(100000):
    benchmarks[savvy_pick(max(list(scores)))] += 1
print(collections.OrderedDict(sorted(benchmarks.items())))


