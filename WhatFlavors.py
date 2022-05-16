def whatFlavors(cost, money):
    prices = []
    indices = dict()
    for i in range(len(cost)):
        if cost[i] < money:
            prices.append(cost[i])
            if cost[i] not in indices.keys():
                indices[cost[i]] = []
            indices[cost[i]].append(i)
    prices.sort()
    lower = prices[0]
    higher = prices[-1]
    lower_count = 0
    higher_count = len(prices) - 1
    while lower_count < higher_count:
        if lower + higher == money:
            lower_index = indices[lower].pop(0) + 1
            higher_index = indices[higher].pop(0) + 1
            print(min(lower_index, higher_index), max(lower_index, higher_index))
            return
        elif lower + higher < money:
            lower_count += 1
            lower = prices[lower_count]
        else:
            higher_count -= 1
            higher = prices[higher_count]
