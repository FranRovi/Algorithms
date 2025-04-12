# Leet Code Algo 2582. Pass The Pillow

def passThePillow(n, time):
    arr_position = 1
    isForward = True
    for i in range(1, time + 1):
        if isForward:
            if arr_position < n:
                arr_position += 1
            elif arr_position == n:
                isForward = False
                arr_position -= 1
        else:
            if arr_position > 1:
                arr_position -= 1
            elif arr_position == 1:
                isForward = True
                arr_position += 1
    return arr_position

print(passThePillow(4,5))
print(passThePillow(3,2))
print(passThePillow(18,38))