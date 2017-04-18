def max_contig_sum(L):
    '''
    L, a list of integers, at least one positive

    Returns the maximum sum of a contiguous subsequence in L
    '''

    total = 0
    current = 0

    for i in L:
        current += i
        if current > total:
            total = current

    if not L:
        return 0
    else:
        if total < max_contig_sum(L[1:]):
            total = max_contig_sum(L[1:])

    return total
