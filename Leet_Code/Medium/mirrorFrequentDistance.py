# Leet Code Distance 3889. Mirror Frequent Distance.

def mirrorFrequency(s):
    hash_mirror = {
        "a":"z","b":"y","c":"x","d":"w","e":"v","f":"u",
        "g":"t","h":"s","i":"r","j":"q","k":"p","l":"o",
        "m":"n","0":"9","1":"8","2":"7","3":"6","4":"5",
        "z":"a","y":"b","x":"c","w":"d","v":"e","u":"f",
        "t":"g","s":"h","r":"i","q":"j","p":"k","o":"l",
        "n":"m","9":"0","8":"1","7":"2","6":"3","5":"4"
    }
    hash_freq = {}
    for char in s:
        if char not in hash_freq:
            hash_freq[char] = 1
        else:
            hash_freq[char] += 1
    chars_used = {}
    total_sum = 0
    for key, value in hash_freq.items():
        if key not in chars_used:
            if hash_mirror[key] in hash_freq:
                temp = hash_freq[hash_mirror[key]]
            else:
                temp = 0
            total_sum += abs(value - temp)
            chars_used[key] = 1
            chars_used[hash_mirror[key]] = 1
    return total_sum

print(mirrorFrequency("ab1z9"))
print(mirrorFrequency("4m7n"))
print(mirrorFrequency("byby"))


