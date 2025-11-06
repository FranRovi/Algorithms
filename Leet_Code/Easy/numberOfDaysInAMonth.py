# Leet Code Algo 1118. Numbers of Days in a Month

def isLeapYear(n):
    if n % 4 == 0 and n % 100 != 0:
        return True
    if n % 100 == 0 and n % 400 == 0:
        return True
    return False

def numberOfDays(year: int, month: int) -> int:
    hash_months = {"1":31, "2":28, "3":31,"4":30, "5":31, "6":30,"7":31,
    "8":31, "9":30, "10":31,"11":30, "12":31}

    isLeap = isLeapYear(year)

    if isLeap and month == 2:
        return hash_months[str(month)] + 1
    return hash_months[str(month)]

print(numberOfDays(1992, 7))
print(numberOfDays(2000, 2))
print(numberOfDays(1900, 2))
print(numberOfDays(1675, 8)) 
 