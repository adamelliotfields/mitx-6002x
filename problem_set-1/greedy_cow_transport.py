def greedy_cow_transport(cows, limit=10):
    cow = sorted(cows, key=cows.get, reverse=True)
    result = []
    while True:
        trip = []
        total = 0
        for i in cow:
            if total + cows[i] <= limit:
                trip.append(i)
                total += cows[i]
        result.append(trip)
        array = []
        for i in cow:
            if i not in trip:
                array.append(i)
        cow = array
        if cow == []:
            break
    return result
