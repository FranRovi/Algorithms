# Leet Code Algo 1228. Missing Number in Arithmetic Progression.

def missingNumber(arr):
    sorted_arr = sorted(arr)
    diff = sorted_arr[1] - sorted_arr[0] if sorted_arr[1] - sorted_arr[0] < sorted_arr[2] - sorted_arr[1] else sorted_arr[2] - sorted_arr[1]
    counter = 1
    if diff == 0:
        return arr[0]
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i+1] - sorted_arr[i] == diff:
            counter += 1
        else:
            return sorted_arr[0] + counter * diff

print(missingNumber([5,7,11,13]))
print(missingNumber([15,13,12]))
print(missingNumber([0,0,0]))
print(missingNumber([1,1,1,1]))