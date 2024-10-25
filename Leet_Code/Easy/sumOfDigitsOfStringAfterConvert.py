# Leet Code Algo 1945. Sum of Digits of String After Convert

def getLucky(s, k):
    alphabet = {
            "a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8", "i":"9", "j":"10", "k":"11", "l":"12", "m":"13", "n":"14", "o":"15", "p":"16", "q":"17", "r":"18", "s":"19", "t":"20", "u":"21", "v":"22", "w":"23", "x":"24","y":"25", "z":"26"
        }
    strSum = ""
    for ele in s:
        strSum += alphabet[ele]
    for i in range(k):
        tempSum = 0
        for j in range(len(strSum)):
            tempSum += int(strSum[j])
        strSum = str(tempSum)
    return int(strSum)

print(getLucky("iiii", 1))
print(getLucky("leetcode", 2))
print(getLucky("zbax", 2)) 