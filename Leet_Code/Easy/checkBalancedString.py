# Leet Code Algo 3340. Check Balanced String

def isBalanced(num):
    oddIndicesSum = 0
    evenIndicesSum = 0
    for i in range(len(num)):
        if i % 2 == 0:
            evenIndicesSum += int(num[i])
        else:
            oddIndicesSum += int(num[i])
    if oddIndicesSum == evenIndicesSum:
        return True
    return False

print(isBalanced("1234"))
print(isBalanced("24123"))