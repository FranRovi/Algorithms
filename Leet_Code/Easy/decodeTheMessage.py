# Leet Code Algo 2325. Decode the Message

def decodeTheMessage(key, message):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    keyNoWhitespace = key.replace(" ", "")
    keyIdx = 0
    answer = ""
    hashKey = {}
    for i in range(len(keyNoWhitespace)):
        if keyNoWhitespace[i] not in hashKey:
            hashKey[keyNoWhitespace[i]] = alphabet[keyIdx]
            keyIdx += 1
    for k in range(len(message)):
        if message[k] not in hashKey:
            answer += " "
        else:
            answer += hashKey[message[k]]
    return answer
    
print(decodeTheMessage('the quick brown fox jumps over the lazy dog', 'vkbs bs t suepuv'))
print(decodeTheMessage('eljuxhpwnyrdgtqkviszcfmabo', 'zwx hnfx lqantp mnoeius ycgk vcnjrdb'))