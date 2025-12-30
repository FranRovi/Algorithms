# Leet Code Algo 2303. Calculate Amount Paid in Taxes

def calculateTaxes(brackets, income):
    total_taxes = 0.0
    if income == 0:
        return total_taxes
    if income >= brackets[0][0]:
        temp = brackets[0][0] * (brackets[0][1] * 0.01)
        total_taxes += temp
        income -= brackets[0][0]
    else:
        return income * (brackets[0][1] * 0.01) 
    for i in range(1, len(brackets)):
        if income >= brackets[i][0] - brackets[i-1][0]:
            temp = (brackets[i][0] - brackets[i-1][0]) * brackets[i][1] * 0.01 
            total_taxes += temp
            income -= (brackets[i][0] - brackets[i-1][0])
        else:
            total_taxes += income * (brackets[i][1] * 0.01)
            income -= (brackets[i][0] - brackets[i-1][0]) 
            break
    return total_taxes


print(calculateTaxes([[3,50],[7,10],[12,25]], 10))
print(calculateTaxes([[1,0],[4,25],[5,5]], 2))
print(calculateTaxes([[2,50]], 0))
print(calculateTaxes([[10,10]], 5))
print(calculateTaxes([[2,7],[3,17],[4,37],[7,6],[9,83],[16,67],[19,29]], 18))