# Leet Code Algo 2515. Shortest Distance to Target String in a Circular Array

def closestTarget(words, target, startIndex):
    min_distance = 101
    counter = 0
    for i in range(startIndex, len(words) + startIndex):
        if words[i % len(words)] == target:
            if counter < min_distance:
                min_distance = counter
                break
        counter += 1
    counter = 0

    for j in range(startIndex, (len(words) - startIndex) * -1, -1):
        if words[j] == target:
            if counter < min_distance:
                min_distance = counter
                break
        counter += 1
    if min_distance == 101:
        return -1
    return min_distance

print(closestTarget(["hello","i","am","leetcode","hello"], "hello", 1))
print(closestTarget(["a","b","leetcode"], "leetcode", 0))
print(closestTarget(["i","eat","leetcode"],"ate", 0))