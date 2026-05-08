# Leet Code Algo 3818. Minimum Prefix to Make Array Strictly Increasing

def minimumPrefixLength(nums):
    len_nums = len(nums)
    temp = [nums[0]]
    for i in range(1,len_nums):
        if nums[i] > nums[i-1]:
            temp.append(nums[i])
        else:
            temp = [nums[i]]
    return len_nums - len(temp)

print(minimumPrefixLength([1,-1,2,3,3,4,5]))
print(minimumPrefixLength([4,3,-2,-5]))
print(minimumPrefixLength([1,2,3,4]))