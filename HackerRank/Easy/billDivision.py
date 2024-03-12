# Hacker Rank Algo Bill Division 

def billDivision(bill, k, b):
    totalSumToDivide = 0
    for i in range(len(bill)):
        if k != i:
            totalSumToDivide += bill[i]
    if b - (totalSumToDivide / 2) > 0:
        print(int(b - (totalSumToDivide / 2)))
    else:
        print("Bon Appetit")

billDivision([3, 10, 2, 9], 1, 12)
billDivision([3, 10, 2, 9], 1, 7)