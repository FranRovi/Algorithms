# Leet Code Algo 1629. Slowest Key

def slowestKey(releaseTimes, keysPressed):
    longest_time_pressed = releaseTimes[0]
    largest_key = keysPressed[0]
    for i in range(1, len(releaseTimes)):
        if releaseTimes[i]-releaseTimes[i-1] > longest_time_pressed:
            longest_time_pressed = releaseTimes[i]-releaseTimes[i-1]
            largest_key = keysPressed[i]  
        elif releaseTimes[i]- releaseTimes[i-1] == longest_time_pressed and keysPressed[i] > largest_key:
            largest_key = keysPressed[i]       
    return largest_key

print(slowestKey([9,29,49,50],"cbcd"))
print(slowestKey([12,23,36,46,62], "spuda"))
print(slowestKey([23,34,43,59,62,80,83,92,97],"qgkzzihfc"))
    