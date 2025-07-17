# Leet Code Algo 3582. Generate Tag for Video Caption

def generateTag(caption):
    caption = caption.lstrip()
    words = caption.split(" ")
    words[0] = words[0].lower()
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    answer = "#" + "".join(words)    
    if len(answer) > 100:
        return answer[:100]
    else:
        return answer
print(generateTag("Leetcode daily streak achieved"))
print(generateTag("can I Go There"))
print(generateTag("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"))