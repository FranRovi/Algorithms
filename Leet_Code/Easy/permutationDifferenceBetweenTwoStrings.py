# Leet Code Algo 3146. Permutation Difference between Two Strings

def findPermutationDifference(s, t):
    # Brute Force
    # totalSum = 0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if s[i] == t[j]:
        #             totalSum += abs(i - j)
        # return totalSum
        totalSum = 0
        hashT = {}
        
        for i in range(len(t)):
            hashT[t[i]] = i
            
        for j in range(len(s)):
            if s[j] in hashT:
                totalSum += abs(j - hashT[s[j]])
                
        return totalSum
    
print(findPermutationDifference("abc","bac"))
print(findPermutationDifference("abcde","edbac"))
