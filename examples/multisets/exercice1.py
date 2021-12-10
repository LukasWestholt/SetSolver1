#!/usr/bin/env python3
# coding: utf-8

from SetSolver1 import search, MODE, MultiMathSetConstDictType, MultiMathSetResultType
from timeit import default_timer as timer

# THIS IS AN EXAMPLE in /examples. See /beispiele.md for more information.

# Here you set your predefined constants.
# Please make sure that you do not assign a variable letter twice.
# Python dictionaries will otherwise only store the last value and overwrite the previous ones.
const_dict = MultiMathSetConstDictType(
    {
        "A": {"p": 2, "q": 1, "r": 2, "t": 2, "u": 4},
        "B": {"p": 1, "q": 5, "s": 5}
    }
)

# Here you set your wanted solution.
result = MultiMathSetResultType({"p": 3, "q": 7, "s": 5})

not_allowed = [MODE.UNION, MODE.COMPLEMENT, MODE.COMPOSITION, MODE.POWER_SET, MODE.CONVERSE_RELATION,
               MODE.REFLEXIVE_CLOSURE, MODE.TRANSITIVE_CLOSURE]

start_time = timer()
search(const_dict, result, not_allowed)
print("Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")
