# Leet Code Algo 3289. The Two Sneaky Numbers of Digitville.

def getSneakyNumbers(nums):
    answer = []
    hashNums = {}
    for i in range(len(nums)):
        if nums[i] not in hashNums:
            hashNums[nums[i]] = 1
        else: 
            hashNums[nums[i]] += 1
    for key, value in hashNums.items():
        if value == 2:
            answer.append(key)
    return answer

print(getSneakyNumbers([0,1,1,0]))
print(getSneakyNumbers([0,3,2,1,3,2]))
print(getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))
