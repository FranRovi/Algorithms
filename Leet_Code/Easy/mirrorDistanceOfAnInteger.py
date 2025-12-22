# Leet Code Algo 3783. Mirror Distance of an Integer.

def mirrorDistance(n):
    str_num = str(n)
    reverse_str_num = ""
    for i in range(len(str_num)-1, -1,-1):
        reverse_str_num += str_num[i]
    return abs(n - int(reverse_str_num))

print(mirrorDistance(25))
print(mirrorDistance(10))
print(mirrorDistance(7))