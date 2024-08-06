# Leet Code Algo 3190. Find Minimum Operations To Make All Elements Divisible By Three

def minimumOperations(nums):
    counter = 0
    # print(len(nums))
    for i in range(len(nums)):
        # print(i, nums[i])
        if (nums[i] + 1) % 3 == 0 or (nums[i] - 1) % 3 == 0:
            # print(nums[i] + 1, nums[i] - 1)
            counter += 1
        # if nums[i] + 2 % 3 == 0 or nums[i] - 2 % 3 == 0:
        #     print(nums[i] + 2, nums[i] - 2)
        #     counter += 2
    return counter

print(minimumOperations([1,2,3,4]))
print(minimumOperations([3,6,9]))  
print(minimumOperations([8])) 