# Leet Code Algo 3595. Once Twice

def onceTwice(nums):
    hash_freq = {}
    for num in nums:
        if num not in hash_freq:
            hash_freq[num] = 1
        else:
            hash_freq[num] += 1
    answer = [0,0]
    for key, value in hash_freq.items():
        if value == 1:
            answer[0] = key
        elif value == 2:
            answer[1] = key
    return answer

print(onceTwice([2,2,3,2,5,5,5,7,7]))
print(onceTwice([4,4,6,4,9,9,9,6,8]))