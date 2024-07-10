# Leet Code 551. Student Attendance Record I

def checkRecord(s):
    counterAbsent = 0
    counterLate = 0
    for i in range(len(s)):
        if counterLate == 3 or counterAbsent >= 2:
            return False
        elif s[i] == "P":
            counterLate = 0
        elif s[i] == "L":
            counterLate += 1
        elif s[i] == "A":
            counterAbsent += 1
            counterLate = 0
    if counterLate >= 3 or counterAbsent >= 2:
        return False
    return True

print(checkRecord("PPALLP"))
print(checkRecord("PPALLL"))