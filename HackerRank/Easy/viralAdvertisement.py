# Hacker Rank Algo Viral Advertisement
import math


def viralAdvertisement(n):
    shared = 5
    liked = 2 # math.floor(5 / 2)
    cumulative = 2
    for i in range(2, n + 1):
        shared = liked * 3
        liked += math.floor(liked / 2)
        cumulative += liked
    return cumulative

print(viralAdvertisement(3))
print(viralAdvertisement(5))