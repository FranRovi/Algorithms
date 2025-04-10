# Leet Code Algo 3178. Find The Child Who Has The Ball After K Seconds

def numberOfChild(n, k):
    arr_position = 0
    isForward = True
    for i in range(k):
        if isForward:
            if arr_position < n - 1:
                arr_position += 1
            elif arr_position == n - 1:
                isForward = False
                arr_position -= 1
        else:
            if arr_position >= 1:
                arr_position -= 1
            elif arr_position == 0:
                isForward = True
                arr_position += 1
    return arr_position

print(numberOfChild(3,5))
print(numberOfChild(5,6))
print(numberOfChild(4,2)) 