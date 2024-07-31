# Leet Code Algo 2119. A Number After a Double Reversal

def isSameAfterReversal(num):
    if num == 0:
        return True
    if str(num)[-1] == "0":
        return False
    return True

print(isSameAfterReversal(526))
print(isSameAfterReversal(1800))
print(isSameAfterReversal(0))