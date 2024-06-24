# Leet Code Algo 2670. Find the Distinct Difference Array

def distinctDifferenceArray(nums):
    answer = []
    setPrefix = set()
    for i in range(len(nums)):
        setSuffix = set()
        setPrefix.add(nums[i])
        for j in range(i+1,len(nums)):
            setSuffix.add(nums[j])
        answer.append(len(setPrefix) - len(setSuffix))
    return answer    

print(distinctDifferenceArray([1,2,3,4,5]))
print(distinctDifferenceArray([3,2,3,4,2]))
            