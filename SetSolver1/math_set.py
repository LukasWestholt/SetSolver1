from __future__ import annotations
from itertools import chain, combinations
import SetSolver1.MODE
from SetSolver1.STATUS import STATUS


class Identity:
    value: frozenset[int]

    def __init__(self, value):
        if type(value) == frozenset:
            self.value = value
        elif type(value) == set or type(value) == list:
            self.value = frozenset(value)
        else:
            raise ValueError("value not found")

        self.math_set = MathSet(self.value, self, STATUS.NONE)

    def __repr__(self):
        return "{0}({1})".format(type(self).__name__, set(self.value))

    def __hash__(self):
        return hash(self.value)


class TinyMathSet(frozenset):
    _total_deep_len = None

    def __repr__(self):
        if self == frozenset():
            return "{}"
        return str(set(self))

    def deep_len(self):
        return sum(el.deep_len() if isinstance(el, TinyMathSet) else 1 for el in self)

    def total_deep_len(self):
        if self._total_deep_len is None:
            self._total_deep_len = sum(el.total_deep_len()+1 if isinstance(el, TinyMathSet) else 1 for el in self)
        return self._total_deep_len


class MathSet:
    value: frozenset[TinyMathSet | int | tuple]
    identity: Identity | None
    way: (int, MathSet | None, MathSet | None) | STATUS

    def __init__(self, value, identity, way):
        """
        init MathSet
        :type value: frozenset | collections.abc.Iterable
        :type identity: Identity | None
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        """
        if type(value) == frozenset:
            self.value = value
        else:
            self.value = frozenset(value)

        self.identity = identity
        if way is None:
            way = STATUS.NONE
        self.way = way

    def __str__(self):
        if self.is_empty():
            return "{}"
        return str(set(self.value))

    def __repr__(self):
        return self.value, self.identity, self.way

    def __hash__(self):
        # Default: hash(x)==id(x)/16
        # https://stackoverflow.com/a/11324771
        # https://docs.python.org/3/glossary.html#term-hashable
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, MathSet):
            return self.value == other.value
        print("NotImplemented Equality Compare")
        return NotImplemented

    def __len__(self):
        """
        :rtype: int
        """
        return len(self.value)

    def type_check(self, y):
        """
        Check if the type of MathSets is comparable
        :type y: MathSet
        """
        if self.identity != y.identity:
            raise TypeError("type_check error")

    def deep_len(self):
        return sum(el.deep_len() if isinstance(el, TinyMathSet) else 1 for el in self.value)

    def total_deep_len(self):
        return sum(el.total_deep_len()+1 if isinstance(el, TinyMathSet) else 1 for el in self.value)

    def walk_way(self, going_by=None):
        if self.way == STATUS.NONE:
            raise ValueError("STATUS.NONE not allowed here")
        if self.way == STATUS.CONST:
            return 0

        mode = SetSolver1.MODE.CHOOSE_BY_INDEX[self.way[0]]
        if going_by is None:
            going_by = mode[2]
            # set to priority of operator
            # to sort equal length like (pow(pow((A-A)))+B) / (pow((pow(A)&B))+B) [Aufgabe 2]
        lt = list()
        for i in mode[1]:
            if self.way[i] is not None:
                lt.append(self.way[i].walk_way())
        return sum(lt) + going_by

    def sort_key(self):
        return self.walk_way(going_by=1), self.walk_way()

    def is_empty(self):
        """
        Is MathSet empty?
        :rtype: bool
        """
        return self.value == frozenset()

    def union(self, y, way=None):
        """
        German: Vereinigungsmenge
        :type y: MathSet
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        self.type_check(y)
        # self.value.union(y.value)
        copy = set(self.value)
        copy.update(y.value)
        return MathSet(copy, self.identity, way)

    def complement(self, y, way=None):
        """
        German: Komplement - Subtraktion von Mengen
        :type y: MathSet
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        self.type_check(y)
        return MathSet(self.value.difference(y.value), self.identity, way)

    def intersection(self, y, way=None):
        """
        German: Schnittmenge
        :type y: MathSet
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        self.type_check(y)
        return MathSet(self.value.intersection(y.value), self.identity, way)

    def power_set(self, way=None):
        """
        German: Potenzmenge
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        return MathSet(
            [TinyMathSet(y) for y in chain.from_iterable(
                combinations(self.value, i) for i in range(len(self) + 1))],
            self.identity, way)

    def composition(self, y, way=None):
        """
        TODO optimization
        German: Verkettung
        :type y: MathSet
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        self.type_check(y)
        lst = list()
        for x1 in self.value:
            for y1 in y.value:
                if x1[1] == y1[0]:
                    lst.append((x1[0], y1[1]))
        return MathSet(lst, self.identity, way)

    def symmetric_difference(self, y, way=None):
        """
        German: Symmetrische Differenz
        :type y: MathSet
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        self.type_check(y)
        return MathSet(self.value.symmetric_difference(y.value), self.identity, way)

    def do(self):
        """
        German: Erstelle Relation aus Menge
        :rtype: MathSet
        """
        items = list()
        for x1 in self.value:
            if type(x1) != int and type(x1) != str:
                return None
            else:
                for x2 in self.value:
                    items.append((x1, x2))
        return MathSet(items, self.identity, STATUS.NONE)

    def converse_relation(self, way=None):
        """
        TODO optimization
        German: Inverse (Umkehrrelation)
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        return MathSet(((x1[1], x1[0]) for x1 in self.value), self.identity, way)

    def reflexive_closure(self, way=None):
        """
        TODO optimization
        German: Reflexive Hülle
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        return MathSet(list(self.value) + [(x3, x3) for x3 in set([x1[x2] for x2 in range(2) for x1 in self.value])],
                       self.identity, way)

    def transitive_closure(self, way=None):
        """
        TODO optimization
        German: Transitive Hülle
        :type way: (int, MathSet | None, MathSet | None) | STATUS
        :rtype: MathSet
        """
        # {(1 , 1) , (2 , #3#) , (#3# , 1)} -> {(1 , 1) , #(2 , 1)# , (2 , 3), (3 , 1)}
        return MathSet(list(self.value) + [(x1[0], x2[1]) for x2 in self.value for x1 in self.value if x1[1] == x2[0]],
                       self.identity, way)

    def is_reflexive(self):
        """
        :rtype: bool
        """
        if self.identity is None:
            return self.value == self.reflexive_closure().value
        return self.identity.math_set.is_subset(self)

    def is_irreflexive(self):
        """
        :rtype: bool
        """
        if self.identity is None:
            """
            One-Line
            return frozenset((x3, x3) for x3 in set([x1[x2] for x2 in range(2) for x1 in self.value])
                             if (x3, x3) in self.value) == frozenset()
            """
            for x1 in self.value:
                if (x1[0], x1[0]) in self.value or (x1[1], x1[1]) in self.value:
                    return False
            return True
        return self.intersection(self.identity.math_set).is_empty()

    def is_subset(self, y):
        """
        is_subset
        :type y: MathSet
        :rtype: MathSet
        """
        # self.value.issubset(y.value)
        self.type_check(y)
        for x1 in self.value:
            if x1 not in y.value:
                return False
        return True

    def is_symmetric_relation(self):
        """
        :rtype: bool
        """
        return self.converse_relation().is_subset(self)

    def is_asymmetric_relation(self):
        """
        :rtype: bool
        """
        return self.intersection(self.converse_relation()).is_empty()

    def is_antisymmetric_relation(self):
        """
        :rtype: bool
        """
        if self.identity is None:
            for x1 in self.value:
                if x1[::-1] in self.value and not x1[0] == x1[1]:
                    return False
            return True
        return self.intersection(self.converse_relation()).is_subset(self.identity.math_set)

    def is_transitive(self):
        """
        :rtype: bool
        """
        return self.value == self.transitive_closure().value

    def is_preorder(self):
        """
        German: Quasiordnung
        :return: bool
        """
        return self.is_reflexive() and self.is_transitive()

    def is_equivalence_relation(self):
        """
        German: Äquivalenzrelation (symmetrische Quasiordnung)
        :return: bool
        """
        return self.is_preorder() and self.is_symmetric_relation()

    def is_non_strict_partial_order(self):
        """
        German: Halbordnung (partielle Ordnung)
        :return: bool
        """
        return self.is_reflexive() and self.is_antisymmetric_relation() and self.is_transitive()

    def is_strict_partial_order(self):
        """
        German: Strikte Ordnung
        :return: bool
        """
        return self.is_irreflexive() and self.is_transitive() and self.is_asymmetric_relation()

    def get_identity(self):
        """
        Menge auf die die binäre Relation beruht
        :rtype: Identity | None
        """
        items = list()
        for x in self.value:
            if type(x) != int and type(x) != str:
                return None
            else:
                items.append((x, x))

        return Identity(items)

    def print_properties(self):
        """
        Print all properties of this set with relations
        :return: None
        """
        print("is_reflexive: " + str(self.is_reflexive()))
        print("is_irreflexive: " + str(self.is_irreflexive()))
        print("is_symmetrisch: " + str(self.is_symmetric_relation()))
        print("is_asymmetrisch: " + str(self.is_asymmetric_relation()))
        print("is_antisymmetrisch: " + str(self.is_antisymmetric_relation()))
        print("is_transitiv: " + str(self.is_transitive()))
