# Leet Code Algo 2255. Count Prefixes of a Given String

def countPrefixes(words, s):
    counter = 0
    for i in range(len(words)):
        tempSize = len(words[i])
        tempList = s[0:tempSize]
        tempStr = ""
        for ele in tempList:
            tempStr += ele
        if words[i] == tempStr:
            counter += 1
    return counter

print(countPrefixes(['a', 'b', 'c', 'ab', 'bc', 'abc'], "abc"))
print(countPrefixes(["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w","gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"], "w"))
