# Leet Code Algo 3450. Maximum Students on a Single Bench

def maxStudentsOnBench(students):
    hash_student = {}
    for i in range(len(students)):
        if students[i][1] not in hash_student:
            hash_student[students[i][1]] = set()
            hash_student[students[i][1]].add((students[i][0]))
        else:
            hash_student[students[i][1]].add(students[i][0])
    sorted_students_tuple = sorted(hash_student.items(), key= lambda x:len(x[1]), reverse=True)
    sortedHashByBench = dict(sorted_students_tuple)
    if len(sortedHashByBench) == 0:
        return 0
    else:
        for key, value in sortedHashByBench.items():
            return len(value)

print(maxStudentsOnBench([[1,2],[2,2],[3,3],[1,3],[2,3]]))
print(maxStudentsOnBench([[1,1],[2,1],[3,1],[4,2],[5,2]]))
print(maxStudentsOnBench([[1,1],[1,1]]))
print(maxStudentsOnBench([]))