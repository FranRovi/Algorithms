# Leet Code Algo 2129. Capitalize The Title

def capitalizeTheTitle(title):
    answer = ""
    titleLowerCase = title.lower()
    titleSplit = titleLowerCase.split(" ")
    for i in range(len(titleSplit)):
        if len(titleSplit[i]) > 2:
            temp = titleSplit[i].capitalize()
        else:
            temp = titleSplit[i]
        answer += temp + " "
    answer = answer.rstrip()
    return answer
    
print(capitalizeTheTitle("capiTalIze tHe title"))
print(capitalizeTheTitle("First leTTer of Each Word"))
print(capitalizeTheTitle("i lOve leetcode"))
    