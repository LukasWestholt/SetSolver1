#!/usr/bin/env python3
# coding: utf-8

from SetSolver1.MODE import TEMPORARY_CREATED_WAY
from SetSolver1.RelationMathSet import RelationMathSet


def do(value):
    """
    German: Erstelle Relation aus Menge
    :rtype: SimpleMathSet
    """
    items = list()
    for x1 in value:
        if type(x1) != int and type(x1) != str:
            return None
        else:
            for x2 in value:
                items.append((x1, x2))
    return RelationMathSet(items, None, TEMPORARY_CREATED_WAY)


def identity_relation(value):
    """
    Identity relation based on the binary relation
    if there are missing values in the binary relation, they will miss in the Identity
    You should not really use this
    :rtype: RelationMathSet | None
    """
    items = list()
    for x in value:
        if type(x) != int and type(x) != str:
            return None
        else:
            items.append((x, x))
    id_relation = RelationMathSet(items, None, TEMPORARY_CREATED_WAY)
    id_relation.is_identity(True)
    return id_relation
