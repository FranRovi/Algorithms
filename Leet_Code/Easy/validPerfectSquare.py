# Leet Code Algo 367. Valid Perfect Square

def isPerfectSquare(num):
    if num == 1:
        return True
    for i in range(1, num):
        if i * i == num:
            return True
        elif i * i > num:
            return False
    
print(isPerfectSquare(16))
print(isPerfectSquare(14))
