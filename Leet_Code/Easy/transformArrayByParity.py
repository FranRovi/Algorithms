# Add Leet Code Algo 3467. Transform Array By Parity

def transform_array(nums):
    answer = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            answer.insert(0,0)
        else:
            answer.append(1)
    return answer

print(transform_array([4,3,2,1]))
print(transform_array([1,5,1,4,2]))