# Leet Code Algo 1086. High Five

def highFive(items):
    hash_st_exams_grades = {}
    for i in range(len(items)):
        if items[i][0] not in hash_st_exams_grades:
            hash_st_exams_grades[items[i][0]] = [items[i][1]]
        else:
            hash_st_exams_grades[items[i][0]].append(items[i][1])
    hash_st_ranking = {}
    for key, value in hash_st_exams_grades.items():
        sortedDecrese = sorted(value, reverse=True)
        average = sum(sortedDecrese[:5]) // 5
        if average not in hash_st_ranking:
            hash_st_ranking[average] = [key]
        else:
            hash_st_ranking[average].append(key)
    answer = []
    for key, value in hash_st_ranking.items():
        for j in range(len(value)):
            answer.append([value[j], key])
    sorted_answer = sorted(answer)
    return sorted_answer

print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
print(highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))
print(highFive([[1,48],[1,44],[1,28],[1,29],[1,93],[2,46],[2,72],[2,37],[2,25],[2,90],[3,42],[3,37],[3,73],[3,23],[3,73],[4,88],[4,34],[4,47],[4,39],[4,10],[5,54],[5,84],[5,26],[5,61],[5,16]]))