# Leet Code Algo 3921. Score Validator

def scoreValidator(events):
    total_score = 0
    counter = 0
    for i in range(len(events)):
        if events[i].isdigit():
            total_score += int(events[i])
        else:
            if len(events[i]) == 1:
                counter += 1
                if counter == 10:
                    break
            else:
                total_score += 1
    return [total_score, counter]

print(scoreValidator(["1","4","W","6","WD"]))
print(scoreValidator(["WD","NB","0","4","4"]))
print(scoreValidator(["W","W","W","W","W","W","W","W","W","W","W"]))