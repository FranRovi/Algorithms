# Leet Code Algo 2299. Strong Password Checker II

def strongPasswordCheckerII(password):
    if len(password) <= 7:
        return False
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    special_arr = ["!","@","#","$","%","^","&","*","(",")","-","+"]

    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return False
        if not has_lower:
            if password[i].islower():
                has_lower = True
        if not has_upper:
            if password[i].isupper():
                has_upper = True
        if not has_digit:
            if password[i].isdigit():
                has_digit = True
        if not has_special:
            if password[i] in special_arr:
                has_special = True
    if password[-1].islower():
        has_lower = True
    if password[-1].isupper():
        has_upper = True
    if password[-1].isdigit():
        has_digit = True
    if password[-1] in special_arr:
        has_special = True
    if has_special == True and has_upper == True and has_lower == True and has_digit == True:
        return True
    return False

print(strongPasswordCheckerII("IloveLe3tcode!"))
print(strongPasswordCheckerII("Me+You--IsMyDream"))
print(strongPasswordCheckerII("1aB!"))
