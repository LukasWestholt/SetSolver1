#!/usr/bin/env python3
# coding: utf-8

from SetSolver1.MathSet import MathSet


class ConstDictType(dict):
    def __init__(self, data):
        """
        Constructor method
        :type data: collections.abc.Mapping
        """
        super().__init__(data)


class ResultType:
    _result: MathSet

    def __init__(self, data):
        """
        Constructor method
        :type data: MathSet
        """
        self._result = data

    def get(self):
        return self._result
