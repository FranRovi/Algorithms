# Leet Algo 2432. The Employee That Worked on the Longest Task

def hardestWorker(n, logs):
    max_time = 0
    task_id = 0
    prev_time = 0
    for i in range(len(logs)):
        if logs[i][1] - prev_time > max_time:
            max_time = logs[i][1] - prev_time
            task_id = logs[i][0] 
        elif logs[i][1] - prev_time == max_time:
            if logs[i][0] < task_id:
                task_id = logs[i][0] 

        prev_time = logs[i][1]
    return task_id

print(hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))
print(hardestWorker(26, [[1,1],[3,7],[2,12],[7,17]]))
print(hardestWorker(2, [[0,10],[1,20]]))