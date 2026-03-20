# Leet Code Algo 3870. Count Commas in Range

def countCommas(n):
    if n < 1000:
        return 0
    else:
        return n - 1000 + 1

print(countCommas(1002))
print(countCommas(998))
print(countCommas(2008))
print(countCommas(99997))