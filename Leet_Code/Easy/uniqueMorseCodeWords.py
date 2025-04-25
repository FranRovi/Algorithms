# Leet Code Algo 804. Unique Morse Code Words

def uniqueMorseRepresentations(words):
    hash_morse = {
        "a": ".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....",
        "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.",
        "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", 
        "y":"-.--", "z":"--.."  
    }
    hash_words = {}
    for i in range(len(words)):
        temp = ""
        word = len(words[i])
        for j in range(word):
            temp += hash_morse[words[i][j]]
        if temp not in hash_words:
            hash_words[temp] = 1
        else:
            hash_words[temp] += 1
    return len(list(hash_words.keys()))

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))
print(uniqueMorseRepresentations(["a"]))     