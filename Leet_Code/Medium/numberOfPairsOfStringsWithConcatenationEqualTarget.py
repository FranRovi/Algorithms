# Leet Code Algo 2023. Number of Pairs of Strings With Concatenation Equal to Target

def numOfPairs(nums, target):
    counter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                if nums[i] + nums[j] == target:
                    counter += 1
    return counter

print(numOfPairs(["777","7","77","77"], "7777"))
print(numOfPairs(["123","4","12","34"], "1234"))
print(numOfPairs(["1","1","1"], "11"))

