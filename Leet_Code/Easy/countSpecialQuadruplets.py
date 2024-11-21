# Leet Code Algo 1995. Count Special Quadruplets

def countQuadruplets(nums):
    counter = 0
    for i in range(len(nums)-3):
        for j in range(i+1,len(nums)-2):
            for k in range(j+1,len(nums)-1):
                for l in range(k+1, len(nums)):
                    if ((nums[i] + nums[j] + nums[k]) == nums[l] and i<j<k<l):
                        counter += 1
    return counter

print(countQuadruplets([1,2,3,6]))
print(countQuadruplets([3,3,6,4,5]))
print(countQuadruplets([1,1,1,3,5]))
