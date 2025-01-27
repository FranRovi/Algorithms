# Leet Code Algo 2309. Greatest English Letter In Upper and Lower Case

def greatestLetter(s):
    hash_lower_char = {}
    hash_upper_char = {}

    for i in range(len(s)):
        if s[i].islower():
            if s[i] not in hash_lower_char:
                hash_lower_char[s[i]] = 1
        else:
            if s[i] not in hash_upper_char:
                hash_upper_char[s[i]] = 1
    answer = []
    for key, value in hash_upper_char.items():
        if key.lower() in hash_lower_char:
            answer.append(key)
    sorted_answer = sorted(answer, reverse=True)
    return "" if len(sorted_answer) == 0 else sorted_answer[0]

print(greatestLetter("lEeTcOdE"))
print(greatestLetter("arRAzFif"))
print(greatestLetter("AbCdEfGhIjK"))