# Leet Code Algo 2525. Categorize Box According to Criteria

def categorizeBox(length, width, height, mass):
    if mass >= 100 and ((length >= 10000 or width >= 10000 or height >= 10000)
            or length * width * height >= 1000000000):
            return "Both"
    elif mass >= 100:
        return "Heavy"
    elif mass >= 100 or ((length >= 10000 or width >= 10000 or height >= 10000)
        or length * width * height >= 1000000000):
        return "Bulky"
    else:
        return "Neither"
    
print(categorizeBox(1000,35,700,300))
print(categorizeBox(200,50,800,50))