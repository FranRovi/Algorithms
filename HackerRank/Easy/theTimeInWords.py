# Hacker Rank Algo. The time in words

def timeInWords(h, m):
    hashTimeToWords = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eigth",
        29: "twenty nine",
    }
    
    if m == 0:
        return str(hashTimeToWords[h]) + " o' clock"
    elif m == 1:
        return str(hashTimeToWords[m]) + " minute past " + hashTimeToWords[h]
    elif m > 1 and m < 30:
        if m == 15:
            return str(hashTimeToWords[m]) + " past " + hashTimeToWords[h]
        else:
            return str(hashTimeToWords[m]) + " minutes past " + hashTimeToWords[h]
    elif m == 30:
        return "half past " + hashTimeToWords[h]
    elif m == 45:
        return "quarter to " + hashTimeToWords[h + 1]
    else:
        temp = 60 - m
        return str(hashTimeToWords[temp]) + " minutes to " + hashTimeToWords[h + 1]

print(timeInWords(5, 47))
print(timeInWords(3, 00))
print(timeInWords(4, 1))
print(timeInWords(7, 15))
print(timeInWords(7, 29))
print(timeInWords(6, 45))
        