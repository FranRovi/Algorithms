# Leet Code Algo 2053. Kth Distinct String in an Array

def kthDistinct(arr, k):
    hash_chars = {}
    removed_chars = set()
    for c in arr:
        if c not in removed_chars:
            if c not in hash_chars:
                hash_chars[c] = 1
            else:
                removed_chars.add(c)
                del hash_chars[c]
    counter = 1
    for key, val in hash_chars.items():
        if counter == k:
            return key
        counter += 1
    return ""

print(kthDistinct(["d","b","c","b","c","a"],2))
print(kthDistinct(["aaa", "aa", "a"],1))
print(kthDistinct(["a", "b", "a"],3))
print(kthDistinct(["c","exjk","nbmg","kgnas","s","oydx","ghpao","c","r","ohdm","fq","ashgg","mm","cc","mymy","w","t","neb","grjdb","cukk","ujyhn","dq","hhuo","qu","seslw","ybulz","iug","rs","kyfu","krz","nw","txnn","r","zpuao","sh","rfc","c","hgr","jfia","egm","gmuuv","gh","x","nfvgv","ibo","al","wn","o","dyu","zgkk","gdzrf","m","ui","xwsj","zeld","muowr","d","xgiu","yfu"],19))