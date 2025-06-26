# Leet Code Algo 744. Find Smallest Letter Greater Than Target

def nextGreatestLetter(letters, target):
    hash_letters = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,
            "l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,
            "w":23,"x":24,"y":25,"z":26}
    letters_set = set(letters)
    max_dif = 25
    answer = letters[0]
    for char in letters_set:
        if (hash_letters[char] > hash_letters[target] and
        abs(hash_letters[char] - hash_letters[target]) < max_dif):
            max_dif = abs(hash_letters[char] - hash_letters[target])
            answer = char
    return answer

print(nextGreatestLetter(["c","f","j"], "a"))
print(nextGreatestLetter(["c","f","j"], "c"))
print(nextGreatestLetter(["x","x","y","y"], "z"))
    