# Hacker Rank Algo. Breaking the records

def breakingTheRecords(scores):
    min = scores[0]
    max = scores[0]
    counterMax = 0
    counterMin = 0
    for i in range(1, len(scores)):
        if scores[i] < min:
            min = scores[i]
            counterMin += 1
        elif scores[i] > max:
            max = scores[i]
            counterMax += 1
    return [counterMax, counterMin]

print(breakingTheRecords([12,24,10,24]))
print(breakingTheRecords([10,5,20,20,4,5,2,25,1]))
print(breakingTheRecords([3,4,21,36,10,28,35,5,24,42]))
    