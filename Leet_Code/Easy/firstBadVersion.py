# Leet Code Algo 278. First Bad Version

def isBadVersion(num):
    if num == 1702766719:
    # if num == 4:
        return True
    else:
        return False

def firstBadVersion(n):    
    leftIdx = 0
    rightIdx = n
    midVal = 0
    while rightIdx >= leftIdx:
        midVal = round((rightIdx + leftIdx) / 2)
        print("leftIdx " + str(leftIdx))
        print("midVal " + str(midVal))
        print("rightIdx " + str(rightIdx))
        
        if isBadVersion(midVal) == False:
            leftIdx = midVal + 1
        else:
            if isBadVersion(midVal - 1) == False:
                return midVal
            else: 
                rightIdx = midVal - 1

# print(firstBadVersion(5))
print(firstBadVersion(2126753390))
# print(firstBadVersion(1))
            