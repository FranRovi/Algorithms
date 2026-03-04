# Leet Code 1678. Goal Parser Interpretation

def goalParserInterpretation(command):
    answer = ""
    idx = 0
    while idx < len(command):
        if command[idx] == "G":
            answer += "G"
            idx += 1
        else:
            if command[idx+1] == ")":
                answer += "o"
                idx += 2
            else:
                answer += "al"
                idx += 4
    return answer