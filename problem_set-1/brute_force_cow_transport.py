def brute_force_cow_transport(cows, limit=10):
    array = []
    for i in get_partitions(cows.keys()):
        array.append(i)
    a = []
    for i in range(len(array)):
        b = []
        for j in range(len(array[i])):
            c = []
            for k in array[i][j]:
                c.append(cows[k])
            if sum(c) > limit:
                break
            b.append(array[i][j])
        if len(b) == len(array[i]):
            a.append(b)
    num = []
    for i in range(len(a)):
        num.append(len(a[i]))
    for i in a:
        if len(i) == min(num):
            return i
