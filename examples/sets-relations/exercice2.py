#!/usr/bin/env python3
# coding: utf-8

from SetSolver1 import search, MODE, RelationMathSetConstDictType, RelationMathSetResultType, \
    RelationMathSetIdentityType
from timeit import default_timer as timer

# THIS IS AN EXAMPLE in /examples. See /beispiele.md for more information.

# Here you can set an identity relation.
identity = RelationMathSetIdentityType({(1, 1), (2, 2), (3, 3)}).get()

# Here you set your predefined constants.
# Please make sure that you do not assign a variable letter twice.
# Python dictionaries will otherwise only store the last value and overwrite the previous ones.
const_dict = RelationMathSetConstDictType(
    {
        "R": {(1, 1), (1, 4), (3, 3), (4, 4)},
        "S": {(2, 3), (3, 1), (3, 2), (3, 4)}
    },
    identity=identity
)

# Here you set your wanted solution.
result = RelationMathSetResultType({(1, 3), (3, 1), (3, 2), (3, 4), (4, 3)}, identity=identity)

not_allowed = [MODE.POWER_SET, MODE.REFLEXIVE_CLOSURE, MODE.TRANSITIVE_CLOSURE,
               MODE.MULTISET_DIFFERENCE, MODE.MULTISET_DISJOINT_UNION]

start_time = timer()
search(const_dict, result, not_allowed)
print("Calculation ended after " + str(round((timer() - start_time) * 1000) / 1000.0) + " sec")
