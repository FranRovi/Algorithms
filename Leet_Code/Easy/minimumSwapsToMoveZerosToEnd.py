# Leet Code Algo 3936. Minimum Swaps to Move Zeros to End

def minimumSwaps(nums):
    arr_zero_idx = []
    len_nums = len(nums)
    for i in range(len_nums):
        if nums[i] == 0:
            arr_zero_idx.append(i)
    counter = 0
    for j in range(len_nums-1, len_nums-1-len(arr_zero_idx), -1):

        if nums[j] != 0:
            counter += 1
    return counter

print(minimumSwaps([0,1,0,3,12]))
print(minimumSwaps([0,1,0,2]))
print(minimumSwaps([1,2,0]))