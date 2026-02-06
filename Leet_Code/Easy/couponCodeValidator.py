# Leet Code 3606. Coupon Code Validator

def validateCoupons(code, businessLine, isActive):
    len_code = len(code)
    answer = []
    hash_business = {"electronics": 0, "grocery": 0, "pharmacy": 0, "restaurant": 0}
    for i in range(len_code):
        if isActive[i] and businessLine[i] in hash_business and len(code[i]) > 0:
            answer.append((code[i], i))
    is_valid_code = True
    for j in range(len(answer)):
        for k in range(len(answer[j][0])):
            if answer[j][0][k].isalnum() or answer[j][0][k] == "_":
                continue
            else:
                is_valid_code = False
                break
        if is_valid_code == False:
            answer.pop(j)
        is_valid_code = True
    hash_answer = {}
    for l in range(len(answer)):
        hash_answer[answer[l]] = businessLine[answer[l][1]]
    sorted_hash_dict = dict(sorted(hash_answer.items(), key=lambda item:(item[1],item[0][0])))
    sorted_answer_arr = []
    for key, value in sorted_hash_dict.items():
        sorted_answer_arr.append(key[0])
    return sorted_answer_arr

print(validateCoupons(["SAVE20","","PHARMA5","SAVE@20"],["restaurant","grocery","pharmacy","restaurant"],[True, True, True, True]))
print(validateCoupons(["GROCERY15","ELECTRONICS_50","DISCOUNT10"],["grocery","electronics","invalid"],[False, True, True]))  
print(validateCoupons(["pBXoMqBU0_aMgc9F8dy6TaSzza3KjSJFjxZa_NuyMjzEBR7fJNwpGHh7lzuoZvQeEUeo6YumHmIOjjchXlzSVa4ItdyDOImQgm","P8rIIUl35MW8yrqRbO0N_IITptYOxz9tOCbPL6d1aIF_hM2sapaDtUzNpmAZRmJQB1WgjLh8bdYADuSRSU21OzttUkq73qiA66","aFWkYookQlHYMXzhVGxbnrXIl1810ws3qHtketHSECHqJoktWXVZGc6ZyeOuzA_VL9zFL9znpIHwbkwJF2bOPQqsz3_0PYgETJ"],["pharmacy","invalid","pharmacy"],[True, True, True]))    