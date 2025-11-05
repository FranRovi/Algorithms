# Leet Code Algo 1507. Reformat Date.

def reformatDate(date):
    hash_months = {"Jan":"01", "Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
    day = ""
    month_word = date[-8:-5]
    year = date[-4:]
    idx = 0
    while date[idx].isnumeric():
        day += date[idx]
        idx += 1
    if len(day) == 1:
        day = "0" + day
    return year + "-" + hash_months[month_word]+ "-" + day

print(reformatDate("20th Oct 2052"))
print(reformatDate("6th Jun 1933"))
print(reformatDate("26th May 1960"))