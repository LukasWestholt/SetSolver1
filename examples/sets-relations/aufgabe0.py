from SetSolver1 import search
from timeit import default_timer as timer

# THIS IS AN EXAMPLE in /examples. See /beispiele.md for more information.

# Here you set your predefined constants.
# Please make sure that you do not assign a variable letter twice.
# Python dictionaries will otherwise only store the last value and overwrite the previous ones.
const_sets: dict[str, set[frozenset | int | tuple]] = {
    "R": {(1, 2), (3, 2)},
    "S": {(1, 1), (2, 3), (3, 1)}
}

# Here you set your wanted solution.
result = {(3, 3)}

not_allowed = [6, 7]

start_time = timer()
search(const_sets, result, not_allowed)
print("Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")