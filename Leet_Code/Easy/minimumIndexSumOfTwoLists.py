# Leet Code Algo 599. Minimum Index Sum of Two Lists

def findRestaurant(list1, list2,):
    minVal = 9999
    answer = []
    hashWordsBothArrays = {}
    for i in range(len(list1)):
        if list1[i] in list2:
            for j in range(len(list2)):
                if list2[j] == list1[i]:
                    hashWordsBothArrays[list1[i]] = i + j
                    break
    for key, value in hashWordsBothArrays.items():
        if value < minVal:
            minVal = value
            answer = []
            answer.append(key)
        elif value == minVal:
            answer.append(key)
    return answer

print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))
print(findRestaurant(["happy","sad","good"],["sad","happy","good"]))