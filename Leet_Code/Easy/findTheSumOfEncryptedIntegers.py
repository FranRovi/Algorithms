# Leet Code Algo 3079. Find The Sum of Encrypted Integers

def sumOfEncryptedInt(nums):
    totalSum = 0
    if len(nums) == 1:
        answer = ''
        tempStr = str(nums[0])
        largest = int(tempStr[0])
        for k in range(1, len(str(nums[0]))):
            if int(tempStr[k]) >= largest:
                largest = int(tempStr[k])
        answer = str(largest) * len(tempStr)
        return int(answer)
    for i in range(len(nums)):
        tempNumStr = str(nums[i])
        tempNumStrLen = len(tempNumStr)
        if tempNumStrLen > 1:
            largest = int(tempNumStr[0])
            for j in range(len(tempNumStr)):
                if int(tempNumStr[j]) > largest:
                    largest = int(tempNumStr[j])
            totalSum += int(str(largest) * tempNumStrLen)
            # print(totalSum)
        else:
            totalSum += nums[i]
    return totalSum

print(sumOfEncryptedInt([1,2,3]))
print(sumOfEncryptedInt([10,21,31]))
print(sumOfEncryptedInt([164]))
print(sumOfEncryptedInt([18,262,369,288,73]))
 