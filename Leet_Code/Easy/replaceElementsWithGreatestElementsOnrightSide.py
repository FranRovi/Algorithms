# Leet Code Algo 1299. Replace Elements with Greatest Element on Right Side

def replaceElements(arr):
    len_arr = len(arr)
    if len_arr == 1:
        return [-1]
    max_val = arr[-1]
    answer = [0] * len(arr)
    answer[-1] = -1
    answer[-2] = max_val
    ptr = len_arr - 3
    for i in range(len_arr-2,0,-1):
        if arr[i] > max_val:
            max_val = arr[i]
        answer[ptr] = max_val
        ptr -= 1 
    return answer

print(replaceElements([17,18,5,4,6,1]))
print(replaceElements([400]))