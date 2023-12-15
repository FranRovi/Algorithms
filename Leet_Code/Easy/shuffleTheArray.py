# Leet Code Algo 1470. Shuffle The Array

def shuffleTheArray(nums, n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i + n])
    return ans

print(shuffleTheArray([2,5,1,3,4,7], 3))
print(shuffleTheArray([1,2,3,4,4,3,2,1], 4))
print(shuffleTheArray([1,1,2,2], 2))