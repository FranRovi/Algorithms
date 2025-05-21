# Leet Code Algo 1502. Can Make Arithmetic Progression From Sequence

def canMakeArithmeticProgression(arr):
    sorted_arr = sorted(arr)
    dif_step = abs(sorted_arr[0] - sorted_arr[1])
    for i in range(1, len(sorted_arr) -1):
        if abs(sorted_arr[i+1] - sorted_arr[i]) != dif_step:
            return False
    return True

print(canMakeArithmeticProgression([3,5,1]))
print(canMakeArithmeticProgression([1,2,4]))
print(canMakeArithmeticProgression([-544, -509, -474, -439, -404, -369, -334, -299, -264, -229, -194, -159, -124, -89, -54, -19, 16]))