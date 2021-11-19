from SetSolver1 import search
from timeit import default_timer as timer

# THIS IS AN EXAMPLE in /examples. See /beispiele.md for more information.

# Here you set your predefined constants.
# Please make sure that you do not assign a variable letter twice.
# Python dictionaries will otherwise only store the last value and overwrite the previous ones.
const_sets: dict[str, set[frozenset | int]] = {
    "U": {3, 5, 6, frozenset({1})},
    "V": {1, 2, 4, 6, frozenset({3})},
    "W": {4, frozenset({2})}
}

# Here you set your wanted solution.
result = {6, frozenset({2})}


start_time = timer()
search(const_sets, result)
print("Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")
