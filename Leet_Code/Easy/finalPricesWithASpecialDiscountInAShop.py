# Leet Code 1475. Final Prices With a Special Discount in a Shop

def finalPricesWithASpecialDiscountInAShop(prices):
    discountedPrices = []
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if j > i and prices[j] <= prices[i]:
                discountedPrices.append(prices[i] - prices[j])
                break
        else:
            discountedPrices.append(prices[i])
    print(discountedPrices)

finalPricesWithASpecialDiscountInAShop([8,4,6,2,3])
finalPricesWithASpecialDiscountInAShop([1,2,3,4,5])
finalPricesWithASpecialDiscountInAShop([10,1,1,6])