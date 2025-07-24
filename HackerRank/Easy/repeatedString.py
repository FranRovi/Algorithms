# Hacker Rank Algo Repeated String

def repeatedString(s, n):
    len_s = len(s)
    counter = 0
    for i in range(len_s):
        if s[i] == "a":
            counter += 1
    num_of_s_in_n = n // len_s
    diff_to_iterate = n - (len_s * num_of_s_in_n)
    answer = 0
    for j in range(diff_to_iterate):
        if s[j] == "a":
            answer += 1
    return answer + counter * num_of_s_in_n

print(repeatedString("abcac", 10))
print(repeatedString("aba", 10))
print(repeatedString("a", 1000000000000))