from itertools import combinations_with_replacement
from SetSolver1.math_set import MathSet, Identity, STATUS
import SetSolver1.helper.update


def tools(t, x, y):
    """
    :type t: int
    :type x: MathSet
    :type y: MathSet
    :rtype: MathSet
    """
    way = (t, x, y)
    match t:
        case 0:
            return x.union(y, way)
        case 1:
            return x.complement(y, way)
        case 2:
            return y.complement(x, way)
        case 3:
            return x.intersection(y, way)
        case 4:
            return x.composition(y, way)
        case 5:
            return y.composition(x, way)
        case 6:
            if x.total_deep_len() >= (overflow / 2):
                return MathSet(frozenset(), x.identity, way)
            return x.power_set(way)
        case 7:
            if y.total_deep_len() >= (overflow / 2):
                return MathSet(frozenset(), y.identity, way)
            return y.power_set(way)
        case 8:
            return x.converse_relation(way)
        case 9:
            return y.converse_relation(way)
        case 10:
            return x.reflexive_closure(way)
        case 11:
            return y.reflexive_closure(way)
        case 12:
            return x.transitive_closure(way)
        case 13:
            return y.transitive_closure(way)
        case _:
            raise ValueError("value not found")


def s_tools(t, x, y):
    """
    :type t: int
    :type x: str
    :type y: str
    :rtype: str
    """
    print("way: " + str(t) + " " + str([x, y])) if DEBUG else None
    match t:
        case 0:
            return "("+x+"+"+y+")"
        case 1:
            return "("+x+"-"+y+")"
        case 2:
            return "("+y+"-"+x+")"
        case 3:
            return "("+x+"&"+y+")"
        case 4:
            return "("+x+"."+y+")"
        case 5:
            return "("+y+"."+x+")"
        case 6:
            return "pow("+x+")"
        case 7:
            return "pow("+y+")"
        case 8:
            return "inverse("+x+")"
        case 9:
            return "inverse("+y+")"
        case 10:
            return "reflexive_cl("+x+")"
        case 11:
            return "reflexive_cl("+y+")"
        case 12:
            return "transitive_cl("+x+")"
        case 13:
            return "transitive_cl("+y+")"
        case _:
            raise ValueError("value not found")


def format_way_helper(operand, item, const_sets, results):
    """
    :type operand: MathSet | None
    :type item: MathSet
    :type const_sets: dict[str, MathSet]
    :type results: set[MathSet]
    :rtype: str
    """
    if operand is None:
        return ""
    elif operand in const_sets.values():
        return list(const_sets.keys())[list(const_sets.values()).index(operand)]
    else:
        for a in results:
            # TODO is this fastest?
            if operand == a:
                return format_way(a, const_sets, results)
    raise SyntaxError(item.way)


def format_way(item, const_sets, results):
    """
    :type item: MathSet
    :type const_sets: dict[str, MathSet]
    :type results: set[MathSet]
    :rtype: str
    """
    if item.way == STATUS.CONST:
        return list(const_sets.keys())[list(const_sets.values()).index(item)]
    operator, operand1, operand2 = item.way
    return s_tools(operator, format_way_helper(operand1, item, const_sets, results),
                   format_way_helper(operand2, item, const_sets, results))


def check_set(check, const_sets, results):
    """
    :type check: MathSet
    :type const_sets: dict[str, MathSet]
    :type results: set[MathSet]
    """
    if check.total_deep_len() <= overflow:
        results.add(check)
        print(format_way(check, const_sets, results) + " --> " + str(check)) if DEBUG else None


def get_valid_results(const_sets, result, results, do_print):
    """
    :type const_sets: dict[str, MathSet]
    :type result: MathSet
    :type results: set[MathSet]
    :type do_print: bool
    :return: set[set]
    """
    valid_results = list()
    for a in results:
        # TODO is this fastest?
        if result.value == a.value:
            valid_results.append(a)
            print("Calculated result: " + format_way(a, const_sets, results) + " --> " + str(a)) if do_print else None
    return valid_results


def search(const_sets, result, not_allowed=None, identity=None, do_print=True):
    """
    :type const_sets: dict[str, set[frozenset | int | tuple] | MathSet]
    :type result: set[frozenset | int | tuple] | MathSet
    :type not_allowed: list
    :type identity: Identity
    :type do_print: bool
    :rtype: list[MathSet] | None
    """

    if not_allowed is None:
        not_allowed = [4, 5, 8, 9, 10, 11, 12, 13]

    # UPDATE const_sets with frozen-sets to const_sets with MathSets
    for y in const_sets.keys():
        if type(const_sets[y]) == set:
            const_sets[y] = MathSet(SetSolver1.helper.update.to_tiny_math_set(const_sets[y]), identity, STATUS.CONST)
    # UPDATE result with frozen-sets to result with MathSets
    result = MathSet(SetSolver1.helper.update.to_tiny_math_set(result), identity, STATUS.CONST)

    if list(const_sets.values()) == set(list(const_sets.values())):
        raise ValueError('the dictionary values of set constants must be unique')

    results: set[MathSet] = set(const_sets.values())

    len_results_old = None
    for len_obj in range(range_int):
        len_results = len(results)
        print(str(round((len_obj/(range_int-1))*100)) + "% / " + str(len_results)) if do_print else None
        if len_results == len_results_old:
            break  # performance optimization
        len_results_old = len_results
        # TODO is sorted results.copy() better?
        for x in results.copy():
            for y in [x for x in range(14) if x not in not_allowed]:
                for z in const_sets.values():
                    new = tools(y, x, z)
                    check_set(new, const_sets, results)
        valid_results = get_valid_results(const_sets, result, results, do_print)
        if len(valid_results) > 0:
            return valid_results

    len_results_old = None
    for len_obj in range(range_int):
        len_results = len(results)
        print("all: " + str(round((len_obj/(range_int-1))*100)) + "% / " + str(len_results)) if do_print else None
        if len_results == len_results_old:
            break  # performance optimization
        len_results_old = len_results
        temp_results_list_for_power_set = results.copy()
        # for x, y in combinations_with_replacement(results, 2):
        for x, y in combinations_with_replacement(sorted(results, key=lambda i: i.sort_key()), 2):
            for c in [x for x in range(14) if x not in not_allowed + [6, 7]]:
                new = tools(c, x, y)
                check_set(new, const_sets, results)
        if 6 not in not_allowed:
            # TODO is sorted temp_results_list_for_power_set better?
            for x in temp_results_list_for_power_set:
                new = MathSet(frozenset(), x.identity, (6, x, None)) if x.total_deep_len() >= (overflow / 2) \
                    else x.power_set((6, x, None))
                # TODO None could be here a MathSet with value = None
                check_set(new, const_sets, results)
        valid_results = get_valid_results(const_sets, result, results, do_print)
        if len(valid_results) > 0:
            return valid_results

    print("Nothing found :(") if do_print else None
    return None


overflow = 30
range_int = 20
DEBUG = False
