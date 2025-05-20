# Leet Code Algo 806. Number of Lines To Write String

def numberOfLines(widths, s):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    hash_alphabet = {}
    current_line_count = 0
    for i in range(len(alphabet)):
        hash_alphabet[alphabet[i]] = widths[i]
    num_lines = 1
    for j in range(len(s)):
        if current_line_count + hash_alphabet[s[j]] <= 100:
            current_line_count += hash_alphabet[s[j]]
        else:
            num_lines += 1
            current_line_count = hash_alphabet[s[j]] 
    return [num_lines, current_line_count]

print(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz"))
print(numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))
