# Leet Code Algo 3963. Create Grid with Exact One Path

def createGrid(m,n):
    temp = "." * (n)
    answer = []
    answer.append(temp)
    for i in range(1, m):
        temp = ""
        for j in range(n):
            temp += "#"
        answer.append(temp)
    for k in range(1, m):
        answer[k] = answer[k][:n-1] + '.'
    return answer

print(createGrid(2,3))
print(createGrid(3,3))
print(createGrid(1,4))
print(createGrid(4,1))