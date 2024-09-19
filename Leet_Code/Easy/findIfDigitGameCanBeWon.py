# Leet Code Algo 3232. Find if Digit Game Can Be Won

def canAliceWin(nums):
    player_1_score = 0 
    player_2_score = 0
    for num in nums:
        if num < 10:
            player_1_score += num 
        else:
            player_2_score += num
    return True if player_1_score != player_2_score else False

print(canAliceWin([1,2,3,4,10]))
print(canAliceWin([1,2,3,4,5,14]))
print(canAliceWin([5,5,5,25]))