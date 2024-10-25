# Leet Code Algo 1304. Find N Unique Integers Sum up to Zero

def sumZero(n):
    answer = []
    for i in range(int(n/2)):
        answer.append(i + 1)
        answer.append((i + 1) * -1)
    if n % 2 != 0:
        answer.append(0)
    return answer

print(sumZero(4))
print(sumZero(5))