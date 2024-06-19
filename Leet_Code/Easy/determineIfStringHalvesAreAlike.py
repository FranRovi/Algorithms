# Leet Code Algo 1704. Determine if String Halves Are Alike

def halvesAreAlike(s):
    counterLeft = 0
    counterRight = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for i in range(int(len(s)/2)):
        if s[i] in vowels:
            counterLeft += 1
    for j in range(int(len(s)/2), len(s)):
        if s[j] in vowels:
            counterRight += 1
    if counterLeft == counterRight:
        return True
    return False

print(halvesAreAlike("book"))
print(halvesAreAlike("textbook"))
            