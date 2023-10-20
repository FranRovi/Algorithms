# Leet Code 1614. Maximum Nesting Depth of the Parentheses

def maximumNestingDepthOfTheParentheses(s):
    maxNum = 0
    temp = 0
    for i in range(len(s)):
        # print(s[i])
        if s[i] == "(":
            temp += 1
            if temp >= maxNum:
                maxNum = temp
        elif s[i] == ")":
            temp -=1
    return maxNum
            
print(maximumNestingDepthOfTheParentheses("(1+(2*3)+((8)/4))+1)"))
print(maximumNestingDepthOfTheParentheses("(1)+((2))+(((3)))"))
