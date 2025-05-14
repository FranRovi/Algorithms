# Leet Code Algo 3492. Maximum Containers on a Ship

def maxContainers(n, w, maxWeigth):
    num_of_cont = n ** 2
    weight_of_cont = w * num_of_cont
    
    if weight_of_cont <= maxWeigth:
        return num_of_cont
    return maxWeigth // w

print(maxContainers(2, 3, 15))
print(maxContainers(3, 5, 20))
print(maxContainers(2, 2, 10))