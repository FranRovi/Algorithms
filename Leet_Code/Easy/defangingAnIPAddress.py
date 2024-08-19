# Leet Code Algo 1108. Defanging an IP Address

def defangIPAddress(address):
    answer = ""
    for i in range(len(address)):
        if address[i] != ".":
            answer += address[i]
        else:
            answer += "[.]"
    return answer

print(defangIPAddress("1.1.1.1"))
print(defangIPAddress("255.100.50.0")) 