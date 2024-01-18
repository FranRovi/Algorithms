# Leet Code Algo 2293. Min Max Game

def minMaxGame(nums):
    # print("nums: " + str(nums))
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        if nums[0] < nums[1]:
            return nums[0]
        else:
            return nums[1]
    else:
        newNums = []
        for i in range(int((len(nums) / 2))):
            if i % 2 == 0:
                if nums[2 * i] < nums[2 * i + 1]:
                    newNums.append(nums[2 * i])
                else:
                    newNums.append(nums[2 * i + 1])
            else:
                if nums[2 * i] > nums[2 * i + 1]:
                    newNums.append(nums[2 * i])
                else:
                    newNums.append(nums[2 * i + 1])
        return minMaxGame(newNums)                    

print(minMaxGame([1,3,5,2,4,8,2,2]))
print(minMaxGame([3]))
print(minMaxGame([7,9]))
print(minMaxGame([9,7]))
print(minMaxGame([5,1]))
print(minMaxGame([70,38,21,22]))
print(minMaxGame([5,1]))