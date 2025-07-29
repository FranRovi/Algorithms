# Hacker Rank Algo Missing Numbers

def missingNumbers(arr, brr):
    hash_arr_one = {}
    hash_arr_two = {}
    for i in range(len(arr)):
        if arr[i] not in hash_arr_one:
            hash_arr_one[arr[i]] = 1
        else:
            hash_arr_one[arr[i]] += 1
    for j in range(len(brr)):
        if brr[j] not in hash_arr_two:
            hash_arr_two[brr[j]] = 1
        else:
            hash_arr_two[brr[j]] += 1
    answer = []
    for key, value in hash_arr_two.items():
        if key not in hash_arr_one or value != hash_arr_one[key]:
            answer.append(key)
    return sorted(answer)

print(missingNumbers([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204]))
print(missingNumbers([11,4,11,7,13,4,12,11,10,14],[11,4,11,7,3,7,10,13,4,8,12,11,10,14,12]))
print(missingNumbers([7,2,5,3,5,3],[7,2,5,4,6,3,5,3]))