# Leet Code Algo 2788. Split Strings by Separator.

def splitWordsBySeparator(words, separator):
    answer = []
    for word in words:
        temp = word.split(separator)
        for i in range(len(temp)):
            if temp[i] != "":
                answer.append(temp[i])
    return answer

print(splitWordsBySeparator(["one.two.three","four.five","six"], "."))
print(splitWordsBySeparator(["$easy$","$problem$"], "$"))
print(splitWordsBySeparator(["|||"], "|"))