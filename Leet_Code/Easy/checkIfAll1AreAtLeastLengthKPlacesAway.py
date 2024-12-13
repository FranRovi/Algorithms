# Leet Code Algo 1437. Check if All 1's Are at Least K Places Away

def kLengthApart(nums, k):
    isFirst = True
    counter = 0
    for num in nums:
        if num == 1:
            if isFirst == False and counter < k:
                return False
            else:
                isFirst = False
                counter = 0
        elif num == 0:
            counter += 1
    return True

print(kLengthApart([1,0,0,0,1,0,0,1],2))
print(kLengthApart([1,0,0,1,0,1],2))