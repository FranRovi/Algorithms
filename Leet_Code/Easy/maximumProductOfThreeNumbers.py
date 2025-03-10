# Leet Code Algo 628. Maximum Product of Three Numbers

def maximumProduct(nums):
    if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
    negative_arr = []
    positive_arr = []
    for i in range(len(nums)):
        if nums[i] < 0:
            negative_arr.append(nums[i])
        else:
            positive_arr.append(nums[i])
    sorted_negative_arr = sorted(negative_arr, reverse=True)
    sorted_positive_arr = sorted(positive_arr)
    
    if len(sorted_negative_arr) == 0:
        return sorted_positive_arr[-3] * sorted_positive_arr[-2] * sorted_positive_arr[-1]
    if len(sorted_positive_arr) == 0:
        return sorted_negative_arr[0] * sorted_negative_arr[1] * sorted_negative_arr[2]

    negative_product = positive_product = 0

    if len(sorted_negative_arr) >= 2:
        negative_product = sorted_negative_arr[-1] * sorted_negative_arr[-2]
    if len(sorted_positive_arr) >= 2:
        positive_product = sorted_positive_arr[-1] * sorted_positive_arr[-2]    
    
    if positive_product < negative_product:
        return negative_product * sorted_positive_arr[-1]
    elif len(sorted_negative_arr) == 0:
        return positive_product * sorted_positive_arr[-3]
    elif len(sorted_positive_arr) <= 2:
        return negative_product * sorted_positive_arr[-1]
    else:
        if positive_product * sorted_positive_arr[-3] > negative_product * sorted_positive_arr[-1]:
            return positive_product * sorted_positive_arr[-3]
        else:
            return negative_product * sorted_positive_arr[-1]

print(maximumProduct([-100,-98,-1,2,3,4]))
print(maximumProduct([-100,-2,-3,1]))
print(maximumProduct([-1,-2,1,2,3]))
print(maximumProduct([-1,-2,-3,-4]))
print(maximumProduct([3,4,0,0,-1,-5]))
print(maximumProduct([-1,-2,-3]))
print(maximumProduct([1,2,3,4]))
print(maximumProduct([1,2,3]))
