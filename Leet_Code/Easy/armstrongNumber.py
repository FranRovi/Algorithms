# Leet Code Algo 1134. Armstrong Number

def isArmstrong(n):
    str_num = str(n)
    total_sum = 0
    for i in range(len(str_num)):
        total_sum += int(str_num[i]) ** len(str_num)
    return True if total_sum == n else False

print(isArmstrong(153))
print(isArmstrong(123))
print(isArmstrong(371))
print(isArmstrong(372))
print(isArmstrong(1634))
print(isArmstrong(1635))
        