# Leet Code 58. Length of Last Word

def lengthOfLastWord(s):    
    splitted_string = s.split()    
    return len(splitted_string[-1])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("     fly me   to  the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))