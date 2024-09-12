# Hacker Rank Algo. Mark and Toys

def maximumToys(prices, k):
    sortedPrices = sorted(prices)
    idx = 0
    totalSum = 0
    while totalSum <= k:
        if totalSum + sortedPrices[idx] <= k:
            totalSum += sortedPrices[idx]
            # print(idx, totalSum)
        else:
            return idx
        idx += 1
        
print(maximumToys([1,2,3,4], 7))
print(maximumToys([1,12,5,111, 200, 1000, 10], 50))