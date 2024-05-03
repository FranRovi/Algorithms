# Hacker Rank Algo Electronics Shop

def electronicShops(keyboards, drives, b):
    maxToSpend = -1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if ((keyboards[i] + drives[j]) <= b and
                (keyboards[i] + drives[j]) > maxToSpend):
                maxToSpend = keyboards[i] + drives[j] 
            # print(keyboards[i], drives[j])
    return maxToSpend
print(electronicShops([3,1],[5,2,8],10))
print(electronicShops([4],[5],5))