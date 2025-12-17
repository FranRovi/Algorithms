# Leet Code Algo 2644. Find the Maximum Divisibility Score

def maxDivScore(nums, divisors):
    counter = 0
    hash_solution = {}
    for i in range(len(divisors)):
        counter = 0
        for j in range(len(nums)):
            if nums[j] % divisors[i] == 0:
                counter += 1
        if (counter) not in hash_solution:
            hash_solution[(counter)] = [divisors[i]]
        else:
            hash_solution[(counter)].append(divisors[i])
    sorted_solution = dict(sorted(hash_solution.items(), reverse=True))
    arr_answer = list(sorted_solution.values())
    return min(arr_answer[0])

print(maxDivScore([2,9,15,50], [5,3,7,2]))
print(maxDivScore([4,7,9,3,9], [5,2,3]))
print(maxDivScore([20,14,21,10], [10,16,20]))