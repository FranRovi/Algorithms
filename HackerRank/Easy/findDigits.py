# Hacker Rank Find Digits Algo

def findDigits(n):
    counter = 0
    nStr = str(n)
    for i in range(len(nStr)):
        if int(nStr[i]) == 0:
            continue
        if n % int(nStr[i]) == 0:
            counter += 1
    return counter

print(findDigits(124))
print(findDigits(111))
print(findDigits(10))