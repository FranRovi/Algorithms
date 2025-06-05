# Leet Code Algo 1196. How Many Apples Can You Put into the Basket

def maxNumberOfApples(weight):
    sorted_weights = sorted(weight)

    total_sum = sum(weight)
    counter = len(weight)

    if total_sum <= 5000:
        return counter

    for i in range(len(sorted_weights) - 1, -1, -1):
        if total_sum > 5000:
            total_sum -= sorted_weights[i]
            counter -= 1
        else:
            break
    return counter

print(maxNumberOfApples([100,200,150,1000]))
print(maxNumberOfApples([900,950,800,1000,700,800])) 
    