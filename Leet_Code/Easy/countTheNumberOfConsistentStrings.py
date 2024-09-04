# Leet Code Algo 1684. Count The Number of Consistent Strings

def countConsistentStrings(allowed, words):
    counter = len(words)
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] not in allowed:
                counter -= 1
                break
    return counter

print(countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
print(countConsistentStrings(allowed = "fstqyienx", words = ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]))