# Leet Code Algo 3683. Earliest Time to Finish One Task

def earliestTime(tasks):
    set_times = set()
    for i in range(len(tasks)):
        for j in range(2):
            temp = tasks[i][0] + tasks[i][1]
            if temp not in set_times:
                set_times.add(temp)
    return min(set_times)

print(earliestTime([[1,6],[2,3]]))
print(earliestTime([[100,100],[100,100],[100,100]]))