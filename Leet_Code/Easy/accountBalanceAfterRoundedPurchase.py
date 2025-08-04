# Leet Code Algo 2806. Account Balance after Rounded Purchase

def accountBalanceAfterPurchase(purchaseAmount):
    balance_dif = 100 - purchaseAmount
    temp_str = str(balance_dif)
    last_digit = temp_str[-1]
    if last_digit in ["0","1","2","3","4","5"]:
        return balance_dif - int(last_digit)
    else:
        return balance_dif - int(last_digit) + 10

print(accountBalanceAfterPurchase(9))
print(accountBalanceAfterPurchase(15))
print(accountBalanceAfterPurchase(10))
    