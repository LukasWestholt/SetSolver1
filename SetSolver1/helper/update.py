#!/usr/bin/env python3
# coding: utf-8

from SetSolver1.TinyMathSet import TinyMathSet


def to_tiny_math_set(data):
    """
    helper method to update to 2021.11.3
    :type data: any
    :rtype: TinyMathSet | any
    """
    if type(data) == frozenset or type(data) == set or type(data) == list:
        lst = list()
        for x in data:
            lst.append(to_tiny_math_set(x))
        return TinyMathSet(lst)
    return data
