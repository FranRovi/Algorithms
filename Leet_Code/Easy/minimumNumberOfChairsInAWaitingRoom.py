# Leet Code Algo 3168. Minimum Number of Chairs in a Waiting Room

def minimumChairs(s):
    max_num_chair = 0
    counter_persons = 0
    for i in range(len(s)):
        if s[i] == "E":
            counter_persons += 1
            if counter_persons > max_num_chair:
                max_num_chair = counter_persons 
        else:
            counter_persons -= 1
    return max_num_chair

print(minimumChairs("EEEEEEE"))
print(minimumChairs("ELELEEL"))
print(minimumChairs("ELEELEELLL"))
