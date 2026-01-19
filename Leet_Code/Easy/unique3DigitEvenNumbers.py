# Leet Code Algo 3483. Unique 3-Digit Even Numbers

from itertools import permutations

def totalNumbers(digits):
    perm_arr = []
    answer = []
    for p in permutations(digits, r=3):
        temp = int("".join(str(num) for num in p))
        perm_arr.append(temp)
    unique_arr = list(set(perm_arr))
    for n in unique_arr:
        if n % 2 == 0 and len(str(n)) == 3:
            answer.append(n)
    return len(answer)

print(totalNumbers([1,2,3,4]))
print(totalNumbers([0,2,2]))
print(totalNumbers([6,6,6]))
print(totalNumbers([1,3,5]))
print(totalNumbers([9,5,2]))
print(totalNumbers([0,0,0]))