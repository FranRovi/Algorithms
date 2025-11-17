# Leet Code Algo 3745. Maximize Expression of Three Elements.

def maximizeExpressionOfThree(nums):
    sorted_nums = sorted(nums) 
    positive_arr = []
    negative_arr = []
    for n in sorted_nums:
        if n <= 0:
            negative_arr.append(n)
        else:
            positive_arr.append(n)
    if len(negative_arr) == 0:
        return positive_arr[-1] + positive_arr[-2] - positive_arr[0]
    elif len(positive_arr) == 0:
        return negative_arr[-1] + negative_arr[-2] - negative_arr[0]
    elif len(positive_arr) == 1:
        return positive_arr[-1] + negative_arr[-1] - negative_arr[0] 
    else:
        return positive_arr[-1] + positive_arr[-2] - negative_arr[0]

print(maximizeExpressionOfThree([1,4,2,5]))
print(maximizeExpressionOfThree([-2,0,5,-2,4]))