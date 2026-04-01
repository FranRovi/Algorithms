# Leet Code Algo 697. Degree of an Array.

def findShortestSubarray(nums):
    hash_frequency = {}
    hash_index = {}
    for i in range(len(nums)):
        if nums[i] not in hash_frequency:
            hash_frequency[nums[i]] = 1
            hash_index[nums[i]] = [i]
        else:
            hash_frequency[nums[i]] += 1
            hash_index[nums[i]].append(i)
    sorted_frequency = dict(sorted(hash_frequency.items(), key=lambda x:x[1], reverse=True))        
    temp = list(sorted_frequency.values())
    prev = temp[0]
    answer = []
    for key, value in sorted_frequency.items():
        if  value == prev:
                answer.append(key)
        else:
            break
    min_val = 50000
    for j in range(len(answer)):
        if abs(hash_index[answer[j]][-1] - hash_index[answer[j]][0]) + 1 < min_val:
            min_val = abs(hash_index[answer[j]][-1] - hash_index[answer[j]][0]) + 1  
    return min_val

print(findShortestSubarray([1,2,2,3,1]))
print(findShortestSubarray([1,2,2,3,1,4,2]))