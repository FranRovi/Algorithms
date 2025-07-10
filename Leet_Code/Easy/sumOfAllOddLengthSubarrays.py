# Leet Code Algo 1588. Sum of all Odd Length Subarrays

def sumOddLengthSubarrays(arr):
    len_arr = len(arr)
    idx = 1
    total_sum = 0
    while idx < len_arr:
        temp = arr[:idx]
        total_sum += sum(temp)
        for i in range(idx,len_arr):
            temp.append(arr[i])
            temp.pop(0)
            total_sum += sum(temp)
        idx += 2
    if len_arr % 2 != 0:
        total_sum += sum(arr)
    return total_sum

print(sumOddLengthSubarrays([1,4,2,5,3]))
print(sumOddLengthSubarrays([1,2]))
print(sumOddLengthSubarrays([10,11,12]))

    