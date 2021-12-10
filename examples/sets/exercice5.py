#!/usr/bin/env python3
# coding: utf-8

from SetSolver1 import search, SimpleMathSetConstDictType, SimpleMathSetResultType
from timeit import default_timer as timer

# THIS IS AN EXAMPLE in /examples. See /beispiele.md for more information.

# Here you set your predefined constants.
# Please make sure that you do not assign a variable letter twice.
# Python dictionaries will otherwise only store the last value and overwrite the previous ones.
const_dict = SimpleMathSetConstDictType(
    {
        "A": {frozenset({2, frozenset({5, frozenset({1})})})},
        "B": {frozenset(), frozenset({5, frozenset()})}
    }
)

# Here you set your wanted solution.
result = SimpleMathSetResultType(
    {frozenset(), frozenset(frozenset({5, frozenset({})})), frozenset({frozenset(frozenset({5, frozenset({})}))})}
)


start_time = timer()
search(const_dict, result)
print("Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")
