# Leet Code Algo. Richest Customer Wealth

def richestCustomerWealth(accounts):
    richestCustomer = 0
    partialSum = 0
    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            partialSum += accounts[i][j]
        if partialSum > richestCustomer:
            richestCustomer = partialSum
        partialSum = 0
    return richestCustomer
            
            
print(richestCustomerWealth([[1,2,3],[3,2,1]]))
print(richestCustomerWealth([[1,5],[7,3],[3,5]]))
print(richestCustomerWealth([[2,8,7],[7,1,3],[1,9,5]]))
