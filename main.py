from itertools import chain, combinations, combinations_with_replacement


def union(x, y):
    """
    German: Vereinigungsmenge
    :type x: set[frozenset | int]
    :type y: set[frozenset | int]
    :rtype: set[frozenset | int]
    """
    x_copy = x.copy()
    x_copy.update(y)
    return x_copy


def complement(x, y):
    """
    German: Komplement - Subtraktion von Mengen
    :type x: set[frozenset | int]
    :type y: set[frozenset | int]
    :rtype: set[frozenset | int]
    """
    return x.difference(y)


def intersection(x, y):
    """
    German: Schnittmenge
    :type x: set[frozenset | int]
    :type y: set[frozenset | int]
    :rtype: set[frozenset | int]
    """
    return x.intersection(y)


def power_set(x):
    """
    German: Potenzmenge
    :type x: set[frozenset | int]
    :rtype: set[frozenset | int]
    """
    if size(x) >= (overflow/2):
        return set()
    return set([frozenset(y) for y in chain.from_iterable(combinations(x, i) for i in range(len(x) + 1))])


def tools(t, x, y):
    """
    :type t: int
    :type x: set[frozenset | int]
    :type y: set[frozenset | int]
    :rtype: set[frozenset | int]
    """
    switcher = {
        0: union(x, y),
        1: complement(x, y),
        2: complement(y, x),
        3: intersection(x, y),
        4: power_set(x),
        5: power_set(y),
    }
    return switcher[t]


def s_tools(t, x, y):
    """
    :type t: int
    :type x: str
    :type y: str
    :rtype: str
    """
    switcher = {
        0: "("+x+"+"+y+")",
        1: "("+x+"-"+y+")",
        2: "("+y+"-"+x+")",
        3: "("+x+"&"+y+")",
        4: "pow("+x+")",
        5: "pow("+y+")"
    }
    return switcher[t]


def size(x):
    """
    :type x: set[frozenset | int] | frozenset
    :rtype: int
    """
    y = 0
    for item in x:
        if type(item) == set or type(item) == frozenset:
            y += size(item)
        y += 1
    return y


def format_set(x):
    """
    :type x: set[frozenset | int]
    :rtype: str
    """

    return str(x).replace("frozenset()", "{}").replace("set()", "{}").replace("frozenset(", "").replace(")", "")


def format_way(x, const_sets, results):
    """
    :type x: list[int, set | None, set | None] | None]
    :type const_sets: dict[str, set[frozenset | int]]
    :type results: list[tuple[set, list[int, set | None, set | None] | None]]
    :rtype: str
    """
    # [c, x, y]
    way = list()
    if x[1] is None:
        way.append("")
    elif x[1] in const_sets.values():
        way.append(list(const_sets.keys())[list(const_sets.values()).index(x[1])])
    else:
        for y in results:
            if x[1] == y[0]:
                way.append(format_way(y[1], const_sets, results))
                break
        if len(way) == 0:
            way.append("")
            print(x)
            input("error 1")

    if x[2] is None:
        way.append("")
    elif x[2] in const_sets.values():
        way.append(list(const_sets.keys())[list(const_sets.values()).index(x[2])])
    else:
        for y in results:
            if x[2] == y[0]:
                way.append(format_way(y[1], const_sets, results))
                break
        if len(way) == 1:
            way.append("")
            print(x)
            input("error 2")
    # print("way: " + str(way))
    return s_tools(x[0], way[0], way[1])


def check_set(check, way, results):
    """
    :type check: set[frozenset | int]
    :type way: list[int, set, set]
    :type results: list[tuple[set, list[int, set | None, set | None] | None]]
    """
    if size(check) <= overflow and check not in [x[0] for x in results]:
        # print(str(check) + ":" + str(way))
        results.append((check, way))


def search(const_sets, result):
    """
    :type const_sets: dict[str, set[frozenset | int]]
    :type result: set[frozenset | int]
    :rtype: bool
    """

    const_sets = unique_set(const_sets)
    results: list[tuple[set, list[int, set | None, set | None] | None]] = [(x, None) for x in const_sets.values()]
    for len_obj in range(range_int):
        print(str(round((len_obj/(range_int-1))*100)) + "% / " + str(len(results)))
        for x, _ in results.copy():
            for y in range(6):
                for z in const_sets.values():
                    new = tools(y, x, z)
                    check_set(new, [y, x, z], results)
        if result in [x[0] for x in results]:
            return end(const_sets, result, results)

    for len_obj in range(range_int):
        print("all: " + str(round((len_obj/(range_int-1))*100)) + "% / " + str(len(results)))
        temp_results_list_for_power_set = results.copy()
        for (x, _), (y, _) in combinations_with_replacement(results, 2):
            for c in range(4):
                new = tools(c, x, y)
                check_set(new, [c, x, y], results)
        for x, _ in temp_results_list_for_power_set:
            new = power_set(x)
            check_set(new, [4, x, None], results)
        if result in [x[0] for x in results]:
            return end(const_sets, result, results)
    return False


def unique_set(x):
    """
    :type x: dict[str, set[frozenset | int]]
    :rtype: dict[str, set[frozenset | int]]
    """
    temp = list()
    for y in x.values():
        if y not in temp:
            temp.append(y)
        else:
            raise ValueError('the dictionary values of set constants must be unique')
    return x


def end(const_sets, result, results):
    print("Calculated result(s):")
    for a, b in results:
        # print(format_way(b, const_sets, results) + " --> " + format_set(a))
        if result == a:
            print(format_way(b, const_sets, results) + " --> " + format_set(a))
    return True


overflow = 30
range_int = 20
