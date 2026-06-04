# Leet Code Algo 3167. Better Compression of String.

def betterCompression(compressed):
    hash_val = {}
    for i in range(0, len(compressed)-1):
        temp = ""
        if compressed[i].isalpha():
            for j in range(i+1, len(compressed)):
                if compressed[j].isdigit():
                    temp += compressed[j]
                else:
                    break
            if compressed[i] not in hash_val:
                hash_val[compressed[i]] = int(temp)
            else:
                hash_val[compressed[i]] += int(temp)
    sorted_hash_val = dict(sorted(hash_val.items()))
    answer = ""
    for key, value in sorted_hash_val.items():
        answer += key + str(value)
    return answer

print(betterCompression("a3c9b2c1"))
print(betterCompression("c2b3a1"))
print(betterCompression("a2b4c1"))