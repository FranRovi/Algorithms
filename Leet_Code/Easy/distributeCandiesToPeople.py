# Leet Code Algo 1103. Distribute Candies to People

def distributeCandies(candies, num_people):
    candies_left = candies - 1
    answer = [0] * (num_people)
    answer[0] = 1
    idx = 0
    while candies_left > 0:
        idx += 1
        temp = (idx + 1)
        if temp >= candies_left:
            answer[idx%num_people] += candies_left
            candies_left = 0
        else:
            answer[idx%num_people] += temp
            candies_left -= temp
    return answer

print(distributeCandies(7,4))
print(distributeCandies(10,3))