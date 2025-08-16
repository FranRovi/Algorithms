# Hacker Rank Algo Max Min.

def maxMin(arr, k):
    sorted_arr = sorted(arr)
    current_arr = sorted_arr[:k]
    min_diff = current_arr[-1] - current_arr[0]
    for i in range(k,len(sorted_arr)):
        current_arr.append(sorted_arr[i])
        current_arr.pop(0)
        if current_arr[-1] - current_arr[0] < min_diff:
            min_diff = current_arr[-1] - current_arr[0]
    return min_diff
    
print(maxMin([1,4,7,2], 2))
print(maxMin([10,100,300,200,1000,20,30], 3))
print(maxMin([1,2,3,4,10,20,30,40,100,200], 4))
print(maxMin([2,1,2,1,2], 2))
    
        
        