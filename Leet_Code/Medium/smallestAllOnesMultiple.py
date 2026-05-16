# Leet Code Algo 3790. Smallest All_Ones Multiple

def minAllOneMultiple(k):
    if k % 2 == 0 or str(k)[-1] == "5":
        return -1
    temp_set = set()
    str_k = str(k)
    for i in range(len(str_k)):
        temp_set.add(int(str_k[i]))
    if len(temp_set) == 1 and 1 in temp_set:
        return len(str(k))
    curr_num = 1 % k
    counter = 1
    while True:
        if curr_num % k == 0:
            return counter
        curr_num = (curr_num * 10 + 1) % k
        counter += 1

print(minAllOneMultiple(3))
print(minAllOneMultiple(7))
print(minAllOneMultiple(2))
print(minAllOneMultiple(15))
print(minAllOneMultiple(8727))
print(minAllOneMultiple(99901))
print(minAllOneMultiple(11))
print(minAllOneMultiple(101))