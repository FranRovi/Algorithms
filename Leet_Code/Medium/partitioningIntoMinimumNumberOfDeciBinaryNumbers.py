# Leet Code Algo 1689. Partinining into Minimum Number of Deci-Binary Numbers

def partitioningIntoMinimumNumbersOfDeciBinaryNumbers(n):
    maxNum = 0
    for i in range(len(n)):
        if int(n[i]) > maxNum:
            maxNum = int(n[i])
            if maxNum == 9:
                break
    return maxNum

print(partitioningIntoMinimumNumbersOfDeciBinaryNumbers('32'))
print(partitioningIntoMinimumNumbersOfDeciBinaryNumbers('82734'))
print(partitioningIntoMinimumNumbersOfDeciBinaryNumbers('27346209830709182346'))

    