# Leet Code Algo 2810. Faulty Keyboard

def finalString(s):
    answer = ""
    for i in range(len(s)):
        if s[i] != 'i':
            answer += s[i]
        else:
            temp = ""
            for k in range(len(answer) -1, -1, -1):
                temp += answer[k]
            # print(temp)
            answer = temp
    return answer


print(finalString("string"))
print(finalString("poiinter"))