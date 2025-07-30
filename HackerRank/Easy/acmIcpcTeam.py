# Hacker Rank Algo. ACM ICPC Team

def acmTeam(topic):
    len_arr = len(topic)
    hash_binary = {}
    
    for i in range(len_arr):
        for j in range(i+1, len_arr):
            counter = 0
            for k in range(len(topic[i])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    counter += 1
            if counter not in hash_binary:
                hash_binary[counter] = 1
            else:
                hash_binary[counter] += 1
    highest_key = 0
    occurencies = 0
    for key, value in hash_binary.items():
        if key > highest_key:
            highest_key = key
            occurencies = value
    return highest_key, occurencies

print(acmTeam(["10101","11110","00010"]))
print(acmTeam(["10101","11100","11010","00101"]))
print(acmTeam(["11101","10101","11001","10111","10000","01110"]))