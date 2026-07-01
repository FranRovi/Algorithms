# Leet Code Algo 3775. Reverse Words With Same Vowel Count

def helperReverse(s):
        answer = ""
        for i in range(len(s)-1,-1,-1):
            answer += s[i]
        return answer
    
    
def reverseWords(s: str) -> str:
    s_words = s.split()
    vowels = {"a": 1,"e": 1,"i": 1,"o": 1,"u": 1}
    answer = s_words[0] + " "
    counter = 0
    for i in range(len(s_words[0])):
        if s_words[0][i] in vowels:
            counter += 1
    for j in range(1, len(s_words)):
        temp = 0
        for k in range(len(s_words[j])):
            if s_words[j][k] in vowels:
                temp += 1
        if temp == counter:
            answer += helperReverse(s_words[j]) + " "
        else:
            answer += s_words[j] + " "
    answer = answer[:-1]
    return answer

print(reverseWords("cat and mice"))
print(reverseWords("book is nice"))
print(reverseWords("banana healthy"))
print(reverseWords("cat bat and mice"))
print(reverseWords("sun one data"))