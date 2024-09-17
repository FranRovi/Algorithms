# Hacker Rank Algo. Gemstones

def gemstones(arr):
    if len(arr) < 2:
        answer = set(arr[0]).intersection(set(arr[1]))
        print("answer: ", answer)
    else:
        answer = set(arr[0]).intersection(set(arr[1]))
        print("answer: ", answer)
        for i in range(2,len(arr)):
            temp = set(arr[i])
            tempDelete = answer.difference(temp)
            # tempIntersection = answer.intersection(temp)
            for ele in tempDelete:
                answer.discard(ele)
            print(i, temp, answer)
        return len(answer)

print(gemstones(['abc', 'abc', 'bc']))
print(gemstones(['abcdde', 'baccd', 'eeabg']))
        