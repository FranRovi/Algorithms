# Leet Code 1773. Count Items Matching a Rule

def countItemsMatchingARule(items, ruleKey, ruleValue):
    counter = 0
    for i in range(len(items)):
        if ruleKey == 'type':
            if items[i][0] == ruleValue:
                counter +=1
        elif ruleKey == 'color':
            if items[i][1] == ruleValue:
                counter +=1
        else:
            if items[i][2] == ruleValue:
                counter +=1
    return counter

print(countItemsMatchingARule([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],["phone", "gold", "iphone"]], "color", "silver"))
print(countItemsMatchingARule([["phone", "blue", "pixel"], ["computer", "silver", "phone"],["phone", "gold", "iphone"]], "type", "phone"))
    