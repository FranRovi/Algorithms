# Hacker Rank Algo Caesar Cipher

def caesarCipher(s, k):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer = ''
    letterToIdxHash = {}
    for i in range(len(letters)):
        letterToIdxHash[letters[i]] = i
    idxToLetterHash = {}
    for j in range(len(letters)):
        idxToLetterHash[j] = letters[j]
    for n in range(len(s)): 
        if s[n].lower() in letterToIdxHash:
            temp = letterToIdxHash[s[n].lower()]
            if s[n].isupper() == False:
                answer += idxToLetterHash[(temp + k) % 26]
            else:
                answer += idxToLetterHash[(temp + k) % 26].upper()
        else:
            answer += s[n]
    return answer

print(caesarCipher("There's-a-starman-waiting-in-the-sky", 3)) 
print(caesarCipher('middle-Outz', 2)) 