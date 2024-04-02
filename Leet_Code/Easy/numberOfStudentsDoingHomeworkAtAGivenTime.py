# Leet Code Algo 1450. Number Of Students Doing Homework at a Given Time

def busyStudents(startTime, endTime, queryTime):
    numOfStudents = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            numOfStudents += 1
    return numOfStudents

print(busyStudents([1,2,3], [3,2,7], 4))
print(busyStudents([4], [4], 4))