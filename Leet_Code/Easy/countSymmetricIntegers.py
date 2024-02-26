# Leet Code Algo 2843. Count Symmetric Integers

def countSymmetricInts(low, high):
    counter = 0
    nums = []
    for i in range(low, high + 1):
        tempStr = str(i)
        if len(tempStr) % 2 == 0:
            startHalf = 0
            endHalf = 0
            midVal = int(int(len(tempStr)) / 2)
            for j in range(midVal):
                startHalf += int(tempStr[j])
                endHalf += int(tempStr[j + midVal])
            if endHalf == startHalf:
                counter += 1
                nums.append(int(tempStr))
    # print(nums, counter)
    return counter

print(countSymmetricInts(1, 100))
print(countSymmetricInts(1200, 1230))