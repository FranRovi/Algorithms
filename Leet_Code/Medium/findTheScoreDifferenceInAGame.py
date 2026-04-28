# Leet Code Algo 3847. Find the Score Difference in a Fame

def scoreDifference(nums):
    player1Score = 0
    player2Score = 0
    activePlayer = 0
    numGame = 0
    for i in range(len(nums)):
        numGame += 1
        if numGame % 6 == 0:
            if activePlayer == 0:
                activePlayer = 1
            else:
                activePlayer = 0
        if nums[i] % 2 != 0:
            if activePlayer == 0:
                activePlayer = 1
            else:
                activePlayer = 0
        if activePlayer == 0:
            player1Score += nums[i]
        else:
            player2Score += nums[i]
    return player1Score - player2Score

print(scoreDifference([1,2,3]))
print(scoreDifference([2,4,2,1,2,1]))
print(scoreDifference([1]))