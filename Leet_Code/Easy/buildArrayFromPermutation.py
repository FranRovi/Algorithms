# Leet Code Algo 1920. Build Array from Permutation 

def buildArrayFromPermutation(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans

print(buildArrayFromPermutation([0,2,1,5,3,4]))
print(buildArrayFromPermutation([5,0,1,2,3,4]))