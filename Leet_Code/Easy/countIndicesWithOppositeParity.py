# Leet Code Algo 3917. Count Indices With Opposite Parity

def countOppositeParity(nums):
    len_nums = len(nums)
    if len_nums == 1:
        return [0]
    odd_idxs = []
    even_idxs = []
    for i in range(len_nums):
        if nums[i] % 2 == 0:
            even_idxs.append(i)
        else:
            odd_idxs.append(i)
    answer = [0] * len_nums
    for j in range(len_nums):
        if nums[j] % 2 == 0:
            answer[j] = len(odd_idxs)
            even_idxs = even_idxs[1:]
        else:
            answer[j] = len(even_idxs)
            odd_idxs = odd_idxs[1:]
    return answer

print(countOppositeParity([1,2,3,4]))
print(countOppositeParity([1]))
print(countOppositeParity([5,1]))
print(countOppositeParity([4,4,5]))
    