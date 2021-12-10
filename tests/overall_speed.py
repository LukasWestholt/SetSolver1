from SetSolver1 import search
from timeit import default_timer as timer

const_dict: dict[str, set[frozenset | int]] = {
    "A": {1, 2},
    "B": {1}
}
result = {frozenset({1, 2}), frozenset({2})}

times = 1000


start_time = timer()
for x in range(times):
    search(const_dict, result)
print("Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")
