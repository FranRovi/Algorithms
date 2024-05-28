# Hacker Rank Counting Valleys

def countingValleys(path):
    level = 0
    valleyCount = 0
    for i in range(len(path)):
        if path[i] == "D":
            if level == 0:
                valleyCount += 1
            level -= 1
        else:
            level += 1
    return valleyCount

print(countingValleys('UDDDUDUU'))
# print(countingValleys('DDUUUUDD'))


        