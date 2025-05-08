# Leet Code Algo 3491. Phone Number Prefix

def phonePrefix(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if len(numbers[i]) <= len(numbers[j]):
                if numbers[i] == numbers[j][:len(numbers[i])]:
                    return False
            else:
                if numbers[j] == numbers[i][:len(numbers[j])]:
                    return False
    return True

print(phonePrefix(["1","2","4","3"]))
print(phonePrefix(["001","007","15","00153"]))
print(phonePrefix(["034","329","318","31"]))