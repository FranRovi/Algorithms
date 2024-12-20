# Leet Code Algo 2042. Check if Numbers Are Ascending in a Sentence

def areNumbersAscending(s):
    sArr = s.split(" ")
    numArr = []
    for char in sArr:
        if char.isdigit():
            numArr.append(int(char))
    for i in range(len(numArr)-1):
        if numArr[i] >= numArr[i+1]:
            return False
    return True

print(areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")) 
print(areNumbersAscending("hello world 5 x 5"))
print(areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))