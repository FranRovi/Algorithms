# Leet Code Algo 1984. Minimum Difference Between Highest and Lowest of K Scores

def minimumDifferenceBetweenHighestAndLowestOfKScores(nums, k):
    if len(nums) == 1:
        return 0
    sorted_nums = sorted(nums)
    temp_arr = sorted_nums[:k]
    min_dif = abs(temp_arr[-1] - temp_arr[0])
    for i in range(k, len(sorted_nums)):
        temp_arr.pop(0)
        temp_arr.append(sorted_nums[i])
        if abs(temp_arr[-1] - temp_arr[0]) < min_dif:
            min_dif = abs(temp_arr[-1] - temp_arr[0]) 
    return min_dif

print(minimumDifferenceBetweenHighestAndLowestOfKScores([90], 1))
print(minimumDifferenceBetweenHighestAndLowestOfKScores([9,4,1,7], 2))
print(minimumDifferenceBetweenHighestAndLowestOfKScores([87063,61094,44530,21297,95857,93551,9918], 6))