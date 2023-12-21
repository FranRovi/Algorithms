# Leet Code Algo 344. Reverse String

def  reverseString(s):
    rightIdx = -1
    for i in range(int(len(s)/2)):
        temp = s[i]
        s[i] = s[rightIdx]
        s[rightIdx] = temp
        rightIdx -= 1


reverseString(["h","e","l","l","o"])
reverseString(["H","a","n","n","a","h"])