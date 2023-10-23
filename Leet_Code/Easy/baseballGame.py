# Leet Code 682. Baseball Game

def baseballGame(operations):
    if len(operations) == 0:
        return 0
    record = []
    totalScore = 0
    for i in range(len(operations)):
        if operations[i] == 'C':
            record.pop()
        elif operations[i] == '+':
            record.append(int(record[-1]) + int(record[-2]))
        elif operations[i] == 'D':
            record.append(2 * int(record[-1]))
        else:
            record.append(int(operations[i]))
    for num in record:
            totalScore += num
    return totalScore

print(baseballGame(["5","2","C","D","+"]))
print(baseballGame(["5","-2","4","C","D","9","+","+"]))
