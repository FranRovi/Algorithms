# Leet Code Algo 1189. Maximum Number of Balloons

def maxNumberOfBalloons(text):
    max_words = 0
    single_letters = ['b','a','n']
    double_letters = ['l','o']
    hash_letters = {}
    for char in text:
        if char in hash_letters:
            hash_letters[char] += 1
        else:
            hash_letters[char] = 1
    for single_letter in single_letters:
        if single_letter not in hash_letters:
            return 0
        else:
            if max_words == 0:
                max_words = hash_letters[single_letter]
            else:
                if max_words > hash_letters[single_letter]:
                    max_words = hash_letters[single_letter]
    for double_letter in double_letters:
        if double_letter not in hash_letters:
            return 0
        else:
            if hash_letters[double_letter] / 2 < max_words:
                max_words = hash_letters[double_letter] // 2
    return max_words

print(maxNumberOfBalloons("nlaebolko"))
print(maxNumberOfBalloons("loonbalxballpoon"))
print(maxNumberOfBalloons("leetcode"))