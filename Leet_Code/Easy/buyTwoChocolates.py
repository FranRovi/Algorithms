# Leet Code Algo 2706. Buy Two Chocolates

# def buyTwoChocolates(prices, money):
#     hashChoco = {}
#     priceTwoChoco = 0
#     chocoNums = 0
#     for i in range(len(prices)):
#         if prices[i] not in hashChoco:
#             hashChoco[prices[i]] = 1
#         else:
#             hashChoco[prices[i]] += 1
#     # print(hashTableCities)
#     sortedTupleChoco = sorted(hashChoco.items())
#     sortedHashChocoByPrice = dict(sortedTupleChoco)
#     print(sortedHashChocoByPrice)
    
    
    # idx = 0
    # for key, value in sortedHashChocoByPrice.items():
    #     if idx < 2:
    #         if value == 2:
    #             return money if priceTwoChoco > money else money - priceTwoChoco
    #         else: 
    #             priceTwoChoco 
    #         print(key)
    #         idx += 1
        
    # for key, value in sortedHashChocoByPrice.items():
    #     if value == 1:
    #         priceTwoChoco += key
    #         chocoNums += 1
    #     elif value 
    #         return money - (key * 2)
    #         break
    #     else:
    #         if chocoNums == 2:
    #             break
    #         else:
    #             priceTwoChoco += key
    #             chocoNums += 1
    #     print(chocoNums, priceTwoChoco)
    # return money if priceTwoChoco > money else money - priceTwoChoco

def buyTwoChocolates(prices, money):
    smallestPrice = 101
    secondSmallestPrice = 102
    
    if prices[0] > prices[1]:
        smallestPrice = prices[1]
        secondSmallestPrice = prices[0]
    else:
        smallestPrice = prices[0]
        secondSmallestPrice = prices[1]
    
    for i in range(2, len(prices)):
        if prices[i] < smallestPrice:
            temp = smallestPrice
            smallestPrice = prices[i]
            secondSmallestPrice = temp
        else:
            if prices[i] < secondSmallestPrice:
                secondSmallestPrice = prices[i]
    # print(smallestPrice, secondSmallestPrice)
    return money if (smallestPrice + secondSmallestPrice) > money else money - (smallestPrice + secondSmallestPrice) 
        
    # smallestPrice = prices[0] + prices[1]
    # for 
    pass
    
    
print(buyTwoChocolates([1,2,2], 3))
print(buyTwoChocolates([3,2,3], 3))
print(buyTwoChocolates([41,1,28,2,92,97,1,87], 68))

