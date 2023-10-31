# Leet Code 2798. Number of Employees Who Met The Target

def numberOfEmployessWhoMetTheTarget(hours, target):
    counter = 0
    for i in range(len(hours)):
        if hours[i] >= target:
            counter += 1
    return counter
print(numberOfEmployessWhoMetTheTarget([0,1,2,3,4], 2))
print(numberOfEmployessWhoMetTheTarget([5,1,4,2,2], 6))