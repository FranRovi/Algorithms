# Leet Code Algo 1544. Make The String Great

def makeGood(s):
    s_list = list(s)
    idx = 0
    s_list_len = len(s_list)
    while idx < s_list_len:
        for i in range(0, s_list_len-1):
            if s_list[i].lower() == s_list[i+1].lower(): 
                if abs(ord(s_list[i]) - ord(s_list[i+1])) == 32:
                # if (s_list[i].isupper() and s_list[i+1].islower()) or (s_list[i].islower() and s_list[i+1].isupper()):
                    s_list.pop(i+1)
                    s_list.pop(i)
                    s_list_len -= 2
                    idx = 0
                    break
        idx += 1
    return "".join(s_list)

print(makeGood("leEeetcode"))
print(makeGood("abBAcC")) 
print(makeGood("s"))
print(makeGood("WpubBUPwG"))
print(makeGood("mC"))
 
                        