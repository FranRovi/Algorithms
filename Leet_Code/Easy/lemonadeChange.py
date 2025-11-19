# Leet Code Algo 860. Lemonade Change

def lemonadeChange(bills):
    if bills[0] != 5:
        return False
    hash_bills = {
        "5":1,
        "10":0,
        "20":0
    }

    for i in range(1, len(bills)):
        hash_bills[str(bills[i])] += 1
        if bills[i] == 10:
            hash_bills["5"] -= 1
            if hash_bills["5"] == -1:
                return False
        elif bills[i] == 20:
            if hash_bills["10"] >= 1 and hash_bills["5"] >= 1:
                hash_bills["5"] -= 1
                hash_bills["10"] -= 1
            elif hash_bills["5"] >= 3:
                hash_bills["5"] -= 3
            else:
                return False
    return True

print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10,10,20]))