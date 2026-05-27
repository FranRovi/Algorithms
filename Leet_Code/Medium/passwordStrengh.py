# Leet Code Algo 3941. Password Strength

def passwordStrength(password):
    hash_chars_used = {}
    total_sum = 0
    for char in password:
        if char not in hash_chars_used:
            hash_chars_used[char] = 1
            if ord(char) <= 57 and ord(char) >= 48:
                total_sum += 3
            elif ord(char) <= 90 and ord(char) >= 65:
                total_sum += 2
            elif ord(char) <= 122 and ord(char) >= 97:
                total_sum += 1
            else:
                if (ord(char) == 33 or ord(char) == 35 or
                ord(char) == 36 or ord(char) == 64):
                    total_sum += 5
    return total_sum

print(passwordStrength("aA1!"))
print(passwordStrength("bbB11#"))