# Leet Code Algo 819. Most Common Word

def mostCommonWord(paragraph, banned):
    paragraph_lower = paragraph.lower()
    paragraph_lower = paragraph_lower.replace(",", " ")
    paragraph_clean = ''.join(ch for ch in paragraph_lower if ch not in ["!","?",",",";",".","'"])
    paragraph_list = paragraph_clean.split()
    hash_words = {}
    for i in range(len(paragraph_list)):
        if paragraph_list[i] not in hash_words:
            hash_words[paragraph_list[i]] = 1
        else:
            hash_words[paragraph_list[i]] += 1
    sorted_words_by_freq = sorted(hash_words.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_words_by_freq)
    for key, value in sorted_dict.items():
        if key not in banned:
            return key

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("a", []))