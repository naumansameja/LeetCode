if len(cost) == 2:
        return 0
    cost.append(0)
    for i in range(len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])

    return cost[-1]