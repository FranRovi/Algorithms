# Leet Code Algo 3852. Smallest Pair With Different Frequencies

def minDistinctFreqPair(nums):
    if len(nums) <= 2:
        return [-1,-1]
    hash_freq = {}
    for num in nums:
        if num not in hash_freq:
            hash_freq[num] = 1
        else:
            hash_freq[num] += 1        
    hash_freq_sorted = {}
    for key, value in hash_freq.items():
        if value not in hash_freq_sorted:
            hash_freq_sorted[value] = [key]
        else:
            hash_freq_sorted[value].append(key)
    sorted_freq_hash = dict(sorted(hash_freq_sorted.items(), key=lambda item:(item[1],item[0])))
    if len(hash_freq_sorted) < 2:
        return [-1,-1]
    answer = [101,102]
    freq = [101,102]
    for key, value in sorted_freq_hash.items():
        for i in range(len(value)):
            if value[i] < answer[0]:
                if key == freq[0]:
                    answer[0] = value[i]
                else:
                    temp = value[i]
                    temp_freq = key 
                    answer[1] = answer[0]
                    freq[1] = freq[0]
                    answer[0] = temp
                    freq[0] = key
            elif value[i] > answer[0] and value[i] < answer[1] and key != freq[0]:
                answer[1] = value[i]
                freq[1] = key 
    return answer

print(minDistinctFreqPair([1,1,2,2,3,4]))
print(minDistinctFreqPair([5,5,4]))
print(minDistinctFreqPair([1,6,6,2,6,1,4]))
print(minDistinctFreqPair([7,3,10,7,7,3,2,9]))
print(minDistinctFreqPair([2,1,4,4]))
print(minDistinctFreqPair([1,1,4,3]))
print(minDistinctFreqPair([5,3,1,4,4]))

