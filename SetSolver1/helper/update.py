from SetSolver1.math_set import TinyMathSet


def to_tiny_math_set(set_of_frozenset_s):
    """
    helper method to update to 2021.11.3
    :type set_of_frozenset_s: set[frozenset | int | tuple] | frozenset | int | tuple
    :rtype: TinyMathSet | int | tuple
    """
    if type(set_of_frozenset_s) == frozenset or type(set_of_frozenset_s) == set:
        items = list()
        for x1 in set_of_frozenset_s:
            items.append(to_tiny_math_set(x1))
        # print(items)
        return TinyMathSet(items)
    return set_of_frozenset_s
