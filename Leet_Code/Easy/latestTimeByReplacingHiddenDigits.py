# Leet Code Algo 1736. Latest Time by Replacing Hidden Digits

def maximumTime(time):
    answer = ["?","?","?","?"]
    if time[0] == "?" and time[1] =="?":
        answer[0] = "2"
        answer[1] = "3"
    if time[3] == "?" and time[4] =="?":
        answer[2] = "5"
        answer[3] = "9"
    if time[0] != "?":
        answer[0] = time[0]
    if time[1] != "?":
        answer[1] = time[1]
    if time[2] != "?":
        answer[2] = time[3]
    if time[4] != "?":
        answer[3] = time[4]
    
    if answer[0] == "?":
        if time[1] == "0" or time[1] == "1" or time[1] == "2" or time[1] == "3":
            answer[0] = "2"
        else:
            answer[0] = "1"
    if answer[1] == "?":
        if time[0] == "1" or time[0] == "0":
            answer[1] = "9"
        else:
            answer[1] = "3"
    if answer[2] == "?":
        if time[3] == "?":
            answer[2] = "5"
    if answer[3] == "?":
        if time[4] == "?":
            answer[3] = "9"

    return answer[0]+answer[1]+":"+answer[2]+answer[3]

print(maximumTime("2?:?0"))
print(maximumTime("0?:3?"))
print(maximumTime("1?:22"))
print(maximumTime("?0:15"))
print(maximumTime("??:3?"))
print(maximumTime("?1:2?"))