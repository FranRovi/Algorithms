# Leet Code Algo 202. Happy Number

def isHappy(n):
    nums = []
    total_sum = 0
    str_n = str(n)
    while True:
        for i in range(len(str_n)):
            total_sum += int(str_n[i]) ** 2
        if total_sum in nums:
            return False
        elif total_sum == 1:
            return True
        nums.append(total_sum)
        str_n = str(total_sum)
        total_sum = 0
        
print(isHappy(19))
print(isHappy(2))
