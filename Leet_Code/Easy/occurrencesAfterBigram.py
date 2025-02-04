# Leet Code Algo 1078. Occurrences After Bigram

def findOccurrences(text, first, second):
    text_lst = text.split(" ")
    answer = []
    for i in range(len(text_lst) - 2):
        if text_lst[i] == first and text_lst[i+1] == second:
            answer.append(text_lst[i+2])
    return answer

print(findOccurrences("alice is a good girl she is a good student", "a", "good"))
print(findOccurrences("we will we will rock you", "we", "will"))