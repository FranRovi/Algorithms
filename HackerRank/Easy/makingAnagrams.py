# Hacker Rank Algo Making Anagrams

def makingAnagrams(s1, s2):
    hash_s1 = {}
    hash_s2 = {}
    counter = 0
    for i in range(len(s1)):
        if s1[i] not in hash_s1:
            hash_s1[s1[i]] = 1
        else:
            hash_s1[s1[i]] += 1
    for j in range(len(s2)):
        if s2[j] not in hash_s2:
            hash_s2[s2[j]] = 1
        else:
            hash_s2[s2[j]] += 1
    for key, value in hash_s1.items():
        if key in hash_s2:
            if value == hash_s2[key]:
                counter += value
            elif value > hash_s2[key]:
                counter += hash_s2[key]
            else:
                counter += value
    return len(s1) + len(s2) - counter * 2

print(makingAnagrams("cde","abc"))
print(makingAnagrams("abc","amnop"))
print(makingAnagrams("absdjkvuahdakejfnfauhdsaavasdlkj","djfladfhiawasdkjvalskufhafablsdkashlahdfa"))