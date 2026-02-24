# Leet Code Algo 3827. Count Monobit Integers

def countMonobit(n):
    set_nums = {0,1,3,7,15,31,63,127,255,511}
    counter = 0
    for i in range(0,n+1):
        if i in set_nums:
            counter += 1
    return counter

print(countMonobit(1))
print(countMonobit(4))