# Leet Code 1528. Shuffle String

def shuffleString(s, indices):
    answerArr = [None] * len(s)
    answer = ""
    for i in range(len(s)):
        answerArr[indices[i]] = s[i]
    for j in range(len(answerArr)):
        answer += answerArr[j]
    return answer


print(shuffleString('codeleet', [4,5,6,7,0,2,1,3]))
print(shuffleString('abc', [0,1,2]))
