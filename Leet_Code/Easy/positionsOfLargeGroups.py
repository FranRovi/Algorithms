# Leet Code Algo 830. Positions of Large Groups

def largeGroupsPositions(s):
    if len(s) <= 2:
        return []
    hash_chars = {}
    for i in range(len(s)):
        if s[i] not in hash_chars:
            hash_chars[str(s[i])] = [i]
        else:
            hash_chars[str(s[i])].append(i)
    answer = []
    for key, value in hash_chars.items():
        counter = 0
        if len(value) >= 3:
            for j in range(1, len(value)):
                if value[j-1] + 1 == value[j]:
                    counter += 1
                else:
                    if counter >= 2:
                        answer.append([value[j-counter-1], value[j-1]])
                    counter = 0
            if counter >= 2:
                answer.append([value[j-counter], value[j]])
    return(sorted(answer))

print(largeGroupsPositions("abbxxxxzzy"))
print(largeGroupsPositions("abc"))
print(largeGroupsPositions("abcdddeeeeaabbbcd"))