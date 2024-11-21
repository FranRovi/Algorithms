# Leet Code Algo 1523. Count Odd Numbers in an Interval Range

def countOdds(low, high):
    if high % 2 == 0:
            high -= 1
    if low % 2 == 0:
        low += 1
    return int((high - low) / 2) + 1

print(countOdds(3,7))
print(countOdds(8,10))