# Leet Code Algo 1561. Maximum Numberof Coins You Can Get

def maxCoins(piles):
    sorted_piles = sorted(piles)
    num_to_pick = int(len(piles) / 3)
    total_sum = 0
    for i in range(num_to_pick, len(piles), 2):
        total_sum += sorted_piles[i]
    return total_sum

print(maxCoins([2,4,1,2,7,8]))
print(maxCoins([2,4,5]))
print(maxCoins([9,8,7,6,5,1,2,3,4]))