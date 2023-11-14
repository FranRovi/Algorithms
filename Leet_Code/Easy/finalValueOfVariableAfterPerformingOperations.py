# Leet Code Algo 2011. Final Value of Variable After Performing Operations
 
def finalValueOfVariableAfterPerformingOperations(operations):
    finalValue = 0
    for i in range(len(operations)):
        # print(operations[i][1])
        if operations[i][1] == '-':
            finalValue -= 1
        elif operations[i][1] == '+':
            finalValue += 1
    return finalValue

print(finalValueOfVariableAfterPerformingOperations(["--X","X++","X++"]))
print(finalValueOfVariableAfterPerformingOperations(["++X","++X","X++"]))
print(finalValueOfVariableAfterPerformingOperations(["X++","++X","--X","X--"]))