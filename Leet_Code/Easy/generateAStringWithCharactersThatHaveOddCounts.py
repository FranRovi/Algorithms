# Leet Code Algo 1374. Generate a String With Characters That Have Odd Counts

def generateTheString(n):
    return "a" * (n-1) + "b" if n % 2 == 0 else "a" * n

print(generateTheString(4))
print(generateTheString(2))
print(generateTheString(7))    