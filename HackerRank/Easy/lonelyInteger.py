# Hacker Rank Algo. Lonely Integer

def lonelyInteger(arr):
    hashNums = {}
    for ele in arr:
        if ele not in hashNums:
            hashNums[ele] = 1
        else:
            del hashNums[ele]
    for item in hashNums.items():
        return item[0]         

print(lonelyInteger([1,2,3,4,3,2,1]))
print(lonelyInteger([1,1,2]))
print(lonelyInteger([0,0,1,2,1]))
    