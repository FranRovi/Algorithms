# Leet Code Algo 1598. Crawler Log Folder

def minOperations(logs):
    curr_level = 0
    for l in logs:
        if l == "../":
            if curr_level > 0:
                curr_level -= 1
        elif l == "./":
            continue
        else:
            curr_level += 1
    return curr_level

print(minOperations(["d1/","d2/","../","d21/","./"]))
print(minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print(minOperations(["d1/","../","../","../"]))