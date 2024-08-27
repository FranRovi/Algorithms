# Leet Code Algo 383. Ransom Note

def canConstruct(ransomNote, magazine):
    hashRansomNote = {}
    hashMagazine = {}
    for i in range(len(ransomNote)):
        if ransomNote[i] not in hashRansomNote:
            hashRansomNote[ransomNote[i]] = 1
        else:
            hashRansomNote[ransomNote[i]] += 1
    for j in range(len(magazine)):
        if magazine[j] not in hashMagazine:
            hashMagazine[magazine[j]] = 1
        else:
            hashMagazine[magazine[j]] += 1
    for key, value in hashRansomNote.items():
        if key not in hashMagazine or value > hashMagazine[key]:
            return False
    return True

print(canConstruct("a","b"))
print(canConstruct("aa","ab"))
print(canConstruct("aa","aab"))