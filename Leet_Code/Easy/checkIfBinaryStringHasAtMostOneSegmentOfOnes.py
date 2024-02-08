# Leet Code Algo 1784. Check if Binary String Has At Most One Segment Of Ones

def checkBinarySegmentsOfOnes(s):
    return "01" not in s

print(checkBinarySegmentsOfOnes("1001"))
print(checkBinarySegmentsOfOnes("110"))