# Leet Code Algo 1176. Diet Plan Performance.

def dietPlanPerformance(calories, k, lower, upper):
    counter = 0
    len_calories = len(calories)
    if k == 1:
        for i in range(len_calories):
            if calories[i] > upper:
                counter += 1
            elif calories[i] < lower:
                counter -= 1 
    else:
        temp_sum = sum(calories[:k])
        if temp_sum > upper:
                counter += 1
        elif temp_sum < lower:
            counter -= 1
        for j in range(k, len_calories):
            temp_sum += calories[j]
            temp_sum -= calories[j-k]
            if temp_sum > upper:
                counter += 1
            elif temp_sum < lower:
                counter -= 1
    return counter

print(dietPlanPerformance([1,2,3,4,5], 1, 3, 3))
print(dietPlanPerformance([3,2], 2, 0, 1))
print(dietPlanPerformance([6,5,0,0], 2, 1, 5))
print(dietPlanPerformance([6,21,0,23,2,9,20,19,22,5,16,23], 2, 1, 21))

