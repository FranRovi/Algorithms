# Hacker Rank Algo Divisible Sum Pairs

def divisibleSumPairs(k, ar):
    counter = 0
    for i in range(len(ar) -1):
        for j in range(i+1, len(ar)):
            # print(ar[i], ar[j])
            if (ar[i] + ar[j]) % k == 0:
                counter += 1
    return counter 
            
print(divisibleSumPairs(3, [1,3,2,6,1,2]))