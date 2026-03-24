# Leet Code Algo 482. License Key Formatting

def licenseKeyFormatting(s, k):
    len_s = len(s)
    chars = []
    for c in s:
        if c.isalpha():
            chars.append(c.upper())
        elif c != "-":
            chars.append(c)
    temp_len = len(chars) + (len(chars) // int(k)) - 1
    if len(chars) % int(k) != 0:
        temp_len += 1
    answer = [0] * temp_len 
    counter = 0
    idx = len(chars) - 1
    for i in range(len(answer) -1, -1, -1):
        if i > 0 and counter == k:
            answer[i] = "-"
            counter = -1
        else:
            answer[i] = chars[idx]
            idx -= 1
        counter += 1
    return "".join(answer)
    
print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("2-5g-3-J", 2))