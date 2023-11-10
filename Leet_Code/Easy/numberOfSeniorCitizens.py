# Leet Code Algo 2678. Number Of Senior Citizens

def numberOfSeniorCitizens(details):
    counter = 0
    for detail in details:
        if int(detail[11] + detail[12]) > 60:
            counter += 1
    return counter
print(numberOfSeniorCitizens(["7868190130M7522","5303914400F9211", "9273338290F4010"]))
print(numberOfSeniorCitizens(["1313579440F2036", "2921522980M5644"]))
print(numberOfSeniorCitizens(["9751302862F0693","3888560693F7262","5485983835F0649","2580974299F6042","9976672161M6561","0234451011F8013","4294552179O6482"]

))
        
        