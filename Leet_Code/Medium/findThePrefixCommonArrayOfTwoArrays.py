def findThePrefixCommonArray(A,B):
    len_arr = len(A)
    answer = []
    for i in range(len_arr -1):
        num_ele = len(set(A[:i+1]).intersection(set(B[:i+1])))
        answer.append(num_ele)
    answer.append(len_arr)
    return answer

print(findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))
print(findThePrefixCommonArray([2,3,1],[3,1,2]))