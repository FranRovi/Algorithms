# Add Leet Code Algo 3304. Find the K-th Character in String Game I

def kthCharacter(k):
    nextChar = {"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h",       "h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}

    answer = "a"

    while len(answer) < k:
        for i in range(len(answer)):
            answer += nextChar[answer[i]]
    return answer[k-1]

print(kthCharacter(5))
print(kthCharacter(10)) 
