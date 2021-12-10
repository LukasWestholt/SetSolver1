from timeit import default_timer as timer
# Is set irreflexive?


def a():
    return frozenset((x3, x3) for x3 in set([x1[x2] for x2 in range(2) for x1 in value]) if (x3, x3) in value) == \
           frozenset()


def b():
    return next((x1 for x1 in value if (x1[0], x1[0]) in value or (x1[1], x1[1]) in value), True)


def c():
    for x1 in value:
        if (x1[0], x1[0]) in value or (x1[1], x1[1]) in value:
            return False
    return True


times = 1000000
value = frozenset({(1, 3), (2, 1), (2, 1), (2, 1), (2, 1), (2, 2), (2, 1)})

start_time = timer()
for x in range(times):
    a()
print("a(): Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")

start_time = timer()
for x in range(times):
    b()
print("b(): Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")

start_time = timer()
for x in range(times):
    c()
print("c(): Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")
