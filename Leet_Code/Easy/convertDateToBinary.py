# Leet Code Algo 3280. Convert Date to Binary

def intToBinary(n):
    reverseBinary = []
    if n == 0:
        reverseBinary = [0]
    elif n == 1:
        reverseBinary = [1]
    else:
        while n >= 2:
            if n % 2 == 0:
                reverseBinary.append(0)
            else:
                reverseBinary.append(1)
            n = n // 2
        reverseBinary.append(1)
    binary_num = []
    for i in range(len(reverseBinary)-1, -1, -1):
        binary_num.append(str(reverseBinary[i]))
    return "".join(binary_num)
    
def convertDateToBinary(date):
    date_split = date.split("-")
    date_nums = []
    for ele in date_split:
        date_nums.append(int(ele))
    date_binary = []
    for ele in date_nums:
        date_binary.append(intToBinary(ele))
    answer = ""
    for ele in date_binary:
        answer += ele + "-"
    return answer[:len(answer)-1]

print(convertDateToBinary("2080-02-29"))
print(convertDateToBinary("1900-01-01"))