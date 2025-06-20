# Leet Code Algo 1624. Largest Substring Between Two Equal Characters

def maxLengthBetweenEqualCharacters(s):
    hash_char = {}
    for i in range(len(s)):
        if s[i] not in hash_char:
            hash_char[s[i]] = [i]
        else:
            hash_char[s[i]].append(i)
    max_length = -1
    for key, value in hash_char.items():
        if len(value) > 1:
            for j in range(len(value)):
                if value[j] - value[0] > max_length:
                    max_length = value[j] - value[0] 
    return max_length -1 if max_length != -1 else max_length

print(maxLengthBetweenEqualCharacters("aa"))
print(maxLengthBetweenEqualCharacters("abca"))
print(maxLengthBetweenEqualCharacters("cbzxy"))
print(maxLengthBetweenEqualCharacters("scayofdzca"))
print(maxLengthBetweenEqualCharacters("cabbac"))
print(maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))