# Leet Code Algo 1880. Check if Word Equals Summation of Two Words

def checkIfWordEqualsSummationOfTwoWords(firstWord, secondWord, targetWord):
    wordVal = {
        'a' : '0',
        'b' : '1',
        'c' : '2',
        'd' : '3',
        'e' : '4',
        'f' : '5',
        'g' : '6',
        'h' : '7',
        'i' : '8',
        'j' : '9',
        'k' : '10',
        'l' : '11',
        'm' : '12',
        'n' : '13',
        'o' : '14',
        'p' : '15',
        'q' : '16',
        'r' : '17',
        's' : '18',
        't' : '19',
        'u' : '20',
        'v' : '21',
        'w' : '22',
        'x' : '23',
        'y' : '24',
        'z' : '25'        
    }
    firstWordSum = ''
    secondWordSum = ''
    targetWordSum = ''
    
    for i in range(len(firstWord)):
        firstWordSum += wordVal[firstWord[i]]
    for j in range(len(secondWord)):
        secondWordSum += wordVal[secondWord[j]]
    for k in range(len(targetWord)):
        targetWordSum += wordVal[targetWord[k]]
    # print(firstWordSum)
    # print(secondWordSum)
    # print(targetWordSum)
    if int(firstWordSum) + int(secondWordSum) == int(targetWordSum):
        return True
    else: return False

print(checkIfWordEqualsSummationOfTwoWords("acb", "cba", "cdb"))
print(checkIfWordEqualsSummationOfTwoWords("aaa", "a", "aab"))