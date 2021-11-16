from itertools import chain, combinations
from timeit import default_timer as timer

# finding the fastest power_set method


def power_set1(x):
    return {frozenset(list(x)[k] for k in range(len(x)) if i & 1 << k) for i in range(2**len(x))}


def power_set2(x):
    return set([frozenset(y) for y in chain.from_iterable(combinations(x, i) for i in range(len(x) + 1))])


def power_set3(x):
    result = [()]
    for i in range(len(x)):
        result += combinations(x, i+1)
    return set([frozenset(x) for x in result])


def power_set4(x):
    result = []
    for i in range(len(x)+1):
        result.extend(combinations(x, i))
    return set([frozenset(x) for x in result])


# example set a
a = {1, 2, 3, frozenset({frozenset()}), frozenset({frozenset({1, 2, 3})})}

start = timer()
r1 = [power_set1(a) for _ in range(100000)]
print((timer() - start) / 100)
# 0.20657684199977666 ms


start = timer()
r2 = [power_set2(a) for _ in range(100000)]
print((timer() - start) / 100)
# 0.1001740360003896 ms

start = timer()
r3 = [power_set3(a) for _ in range(100000)]
print((timer() - start) / 100)
# 0.12723157199972776 ms

start = timer()
r4 = [power_set4(a) for _ in range(100000)]
print((timer() - start) / 100)
# 0.13063165200001095 ms
