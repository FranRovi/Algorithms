# Leet Code Algo 2895. Minimum Processing Time

def minProcessingTime(processorTime, tasks):
    sorted_tasks = sorted(tasks, reverse = True)
    sorted_processor_time = sorted(processorTime)
    hash_nums = {}
    idx = -1
    for i in range(len(sorted_tasks)):
        if i % 4 == 0:
            idx += 1
            temp = sorted_tasks[i] + sorted_processor_time[idx]
            if temp not in hash_nums:
                hash_nums[temp] = 1
        else:
            temp = sorted_tasks[i] + sorted_processor_time[idx]
            if temp not in hash_nums:
                hash_nums[temp] = 1
    return max(list(hash_nums.keys()))

print(minProcessingTime([8,10],[2,2,3,1,8,7,4,5]))
print(minProcessingTime([10,20], [2,3,1,2,5,8,4,3]))
print(minProcessingTime([121,99],[287,315,293,260,333,362,69,233]))