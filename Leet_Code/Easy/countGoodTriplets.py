# Leet Code Algo 1534. Count Good Triplets

def countGoodTriplets(arr, a, b, c):
    counter = 0
    for i in range(len(arr) -2):
        for j in range(i +1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if (abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and
                abs(arr[i] - arr[k]) <= c):
                    counter += 1
    return counter

print(countGoodTriplets([3,0,1,1,9,7], 7,2,3))
print(countGoodTriplets([1,1,2,2,3], 0,0,1))