# Hacker Rank Algo Ice Cream Parlor

def iceCreamParlor(m, arr):
    answer = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == m:
                answer.append(i+1)
                answer.append(j+1)
                # print(answer)
                return answer
print(iceCreamParlor(4, [1,4,5,3,2]))
print(iceCreamParlor(4, [2,2,4,3]))
