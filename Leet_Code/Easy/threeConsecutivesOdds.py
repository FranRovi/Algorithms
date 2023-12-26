# Leet Code Algo 1550. Three Consecutive Odds

def threeConsecutiveOdds(arr):
    countOdds = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            countOdds += 1
            if countOdds > 2:
                return True
        else:
            countOdds = 0
    return False

print(threeConsecutiveOdds([2,6,4,1]))
print(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))