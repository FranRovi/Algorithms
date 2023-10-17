# Leet Code 1512. Number of Good Pairs

def numberOfGoodPairs(nums):
    counter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                counter += 1
    return counter


if __name__ == '__main__':
    print(numberOfGoodPairs([1,2,3,1,1,3]))
    print(numberOfGoodPairs([1,1,1,1]))
    print(numberOfGoodPairs([1,2,3]))

 