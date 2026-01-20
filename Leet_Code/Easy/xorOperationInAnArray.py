# Leet Code Algo 1486. XOR Operation in an Array

def xorOperation(n , start):
    nums_arr = [0] * n
    idx = 0
    for i in range(start, start+n):
        nums_arr[idx] = start + 2 * idx
        idx += 1
    temp = nums_arr[0]
    for j in range(1, n):
        temp ^= nums_arr[j]
    return temp

print(xorOperation(5, 0))
print(xorOperation(4, 3))