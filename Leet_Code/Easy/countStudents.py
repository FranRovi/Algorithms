# Mejorarlo con un circular buffer

def countStudents(students, sandwiches):
    studentsCount = len(students)
    counter = 0
    while (studentsCount > counter):
        activeStudent = students.pop(0)
        if (activeStudent == sandwiches[0]):
            sandwiches.pop(0)
            studentsCount = studentsCount - 1
            counter = 0
        else:
            students.append(activeStudent)
            counter = counter + 1
    return studentsCount

print(countStudents([1,1,0,0],[0,1,0,1]))
print(countStudents([1,1,1,0,0,1],[1,0,0,0,1,1]))
    
        