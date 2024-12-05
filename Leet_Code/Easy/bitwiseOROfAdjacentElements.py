# Leet Code Algo 3173. Bitwise OR Of Adjacent Elements

def orArray(nums):
    answer = []
    for i in range(1, len(nums)):
        answer.append(nums[i-1]| nums[i])
    return answer

print(orArray([1,3,7,15]))
print(orArray([8,4,2]))
print(orArray([5,4,9,11]))