# Leet Code Algo 3687. Library Late Fee Calculator

def lateFee(daysLate):
    total_penalty = 0
    for n in daysLate:
        if n == 1:
            total_penalty += 1
        elif n <= 5 and n >= 2:
            total_penalty += n * 2
        else:
            total_penalty += n * 3
    return total_penalty

print(lateFee([5,1,7]))
print(lateFee([1,1]))