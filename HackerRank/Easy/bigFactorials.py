def bigFactorials(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)
bigFactorials(5)
bigFactorials(25)