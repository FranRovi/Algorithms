# Leet Code Algo 1356. Sort Integers by The Number of 1 Bits

def intToBit(n):
    reversedBit = []
    count_of_ones = 0
    while n >= 2:
        if n % 2 == 0:
            reversedBit.append(0)
        else:
            reversedBit.append(1)
        n = n // 2
    reversedBit.append(1)
    for i in range(len(reversedBit)):
        if reversedBit[i] == 1:
            count_of_ones += 1
    return count_of_ones

def sortByBits(arr):
    hash_one_bit = {}
    for i in range(len(arr)):
        temp_count_one = intToBit(arr[i])
        if temp_count_one not in hash_one_bit:
            hash_one_bit[temp_count_one] = [arr[i]]
        else:
            hash_one_bit[temp_count_one].append(arr[i])
    sorted_fhash_one_bit = sorted(hash_one_bit.items(), key=lambda x:x)
    converted_dict = dict(sorted_fhash_one_bit)
    answer = []
    values = list(converted_dict.values())
    for j in range(len(values)):
        temp_sorted = sorted(values[j])
        for k in range(len(temp_sorted)):
            answer.append(temp_sorted[k])
    return answer

print(sortByBits([0,1,2,3,4,5,6,7,8]))
print(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))