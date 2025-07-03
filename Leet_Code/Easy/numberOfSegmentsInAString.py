# Leet Code Algo 434. Number of Segments in a String

def countSegments(s):
    words_arr = s.split()
    return len(words_arr)

print(countSegments("Hello, my name is John"))
print(countSegments("Hello"))