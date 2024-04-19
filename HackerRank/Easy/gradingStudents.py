# Hacker Rank Algo Grading Students

def gradingStudents(grades):
    for i in range(1, len(grades)):
        # print(i)
        if grades[i] >= 37:
            tempStr = str(grades[i])
            print(tempStr)
            if int(tempStr[-1]) == 3 or int(tempStr[-1]) == 4: 
                #tempStr = tempStr.rstrip(tempStr[-1])
                tempStr = tempStr[0]
                tempStr += '5'
                roundedNum = int(tempStr)
                grades[i] = roundedNum
            elif int(tempStr[-1]) == 8 or int(tempStr[-1]) == 9:
                if int(tempStr) == 99:
                    grades[i] = 100
                else:
                    print(tempStr)
                    #tempStr = tempStr.rstrip(tempStr[-1])
                    tempStr = tempStr[0]
                    tempStr += '0'
                    print(tempStr)
                    roundedNum = int(tempStr) + 10
                    grades[i] = roundedNum
    del grades[0]
    return grades

print(gradingStudents([4,73,67,38,33,88])) 

# print(gradingStudents([3,84,29,57]))
# print(gradingStudents([44,84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40,14,4,29,98,37,23,46,9,79,62,20,38,51,99,59,47,4,86,61,68,17,45,6,1,95,95]))
# print(gradingStudents([33,76,20,23,95,7,60,29,70,16,88,93,63,81,29,63,10,88,46,81,22,18,42,90,89,54,32,81,12,90,35,32,91,95]))