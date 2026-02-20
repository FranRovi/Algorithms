# Leet Code Algo 3846. Total Distance to Type a String Using One Finder

def totalDistance(s):
    len_s = len(s)
    hash_chars = {
        "q":[0,0],"w":[0,1],"e":[0,2],"r":[0,3],"t":[0,4],"y":[0,5],"u":[0,6],"i":[0,7],"o":[0,8],"p":[0,9],
        "a":[1,0],"s":[1,1],"d":[1,2],"f":[1,3],"g":[1,4],"h":[1,5],"j":[1,6],"k":[1,7],"l":[1,8],
        "z":[2,0],"x":[2,1],"c":[2,2],"v":[2,3],"b":[2,4],"n":[2,5],"m":[2,6]
    }
    if len_s == 1:
        return abs(hash_chars[s[0]][0] - 1) + abs(hash_chars[s[0]][1] - 0) 
    total_sum = 0
    prev = [1,0]
    for i in range(len_s):
        total_sum += abs(hash_chars[s[i]][0] - prev[0]) + abs(hash_chars[s[i]][1] - prev[1])
        prev[0] = hash_chars[s[i]][0]
        prev[1] = hash_chars[s[i]][1] 
    return total_sum

print(totalDistance("hello"))
print(totalDistance("a"))