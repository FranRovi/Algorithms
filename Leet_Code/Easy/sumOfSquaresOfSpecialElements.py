# Leet Code Algo 2778. Sum of Squares of Special Elements

def sumOfSquaresOfSpecialElements(nums):
    answer = 0
    for i in range(len(nums)):
        if len(nums) % (i+1) == 0:
            answer += nums[i] * nums[i]
    return answer

print(sumOfSquaresOfSpecialElements([1,2,3,4]))
print(sumOfSquaresOfSpecialElements([2,7,1,19,18,3]))