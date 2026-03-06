# Leet Code Algo 2399. Check Distances Between Same Letters

def checkDistances(s, distance):
    hash_chars = {
        "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,
        "o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25
    }
    hash_distance = {
        "a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],
        "n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]
    }
    for i in range(len(s)):
        hash_distance[s[i]].append(i)
    idx = 0
    for key, value in hash_distance.items():
        if len(value) == 0:
            continue
        else:
            if distance[hash_chars[key]] != value[1] - (value[0] + 1):
                return False 
        idx += 1
    return True

print(checkDistances("abaccb", [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(checkDistances("aa", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(checkDistances("zz", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]))