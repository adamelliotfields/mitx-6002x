def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """

    combs = []
    for x in range(2**len(choices)):
        d = bin(x)[2:]
        while len(d) < len(choices):
            d = '0' + d
        combs.append([int(i) for i in d])

    comb_array = np.array(combs)

    products_equal = [x for x in comb_array if sum(choices * x) == total]

    if products_equal:
        return min(products_equal, key=sum)
    else:
        products_under = [x for x in comb_array if sum(choices * x) < total]
        return max(products_under, key=sum)
