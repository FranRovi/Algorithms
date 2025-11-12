# Leet Code Algo 3736. Minimum Moves To Equal Array Elements III

def minMoves(nums):
    return max(nums) * len(nums) - sum(nums)
        
    # max_num = 0
    # total_sum = 0
    # for n in nums:
    #     if n > max_num:
    #         max_num = n
    #     total_sum += n
    # return len(nums) * max_num - total_sum

print(minMoves([2,1,3]))
print(minMoves([4,4,5]))
    