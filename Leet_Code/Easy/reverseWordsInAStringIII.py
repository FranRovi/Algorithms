# Leet Code Algo 557. Reverse Words in a String III

def reverseWordsInAStringIII(s):
    reverseWords = ''
    sList = s.split(" ")
    for i in range(len(sList)):
        for j in range(len(sList[i]) - 1, -1, -1):
            reverseWords += sList[i][j]
        reverseWords += " "
    reverseWords = reverseWords.rstrip()
    return reverseWords
        
print(reverseWordsInAStringIII("Let's take LeetCode contest"))
print(reverseWordsInAStringIII("Mr Ding"))
        
