# Leet Code Algo 3751. Total Waviness of Numbers in Range I

def totalWaviness(num1, num2):
    counter = 0
    for i in range(num1,num2+1):
        temp_num_str = str(i)
        for j in range(1, len(temp_num_str)-1):
            if temp_num_str[j-1] < temp_num_str[j] and temp_num_str[j] > temp_num_str[j+1]:
                counter += 1
            if temp_num_str[j-1] > temp_num_str[j] and temp_num_str[j] < temp_num_str[j+1]:
                counter += 1
    return counter

print(totalWaviness(120, 130))
print(totalWaviness(198, 202))
print(totalWaviness(4848, 4848))