# Leet Code Algo 1805. Number of Different Integers in a String.

def numDifferentIntegers(word):
    temp_num = ""
    hash_nums = {}
    counter = 0
    for i in range(len(word)):
        if word[i].isdigit():
            temp_num += word[i]
        else:
            if len(temp_num) >= 1:
                if int(temp_num) not in hash_nums:
                    hash_nums[int(temp_num)] = 1
                    temp_num = ""
                    counter += 1
                else:
                    temp_num = ""
    if len(temp_num) >= 1:
        if int(temp_num) not in hash_nums:
            hash_nums[int(temp_num)] = 1
            temp_num = ""
            counter += 1
    return counter

print(numDifferentIntegers("a123bc34d8ef34"))
print(numDifferentIntegers("leet1234code234")) 
print(numDifferentIntegers("a1b01c001"))  
 