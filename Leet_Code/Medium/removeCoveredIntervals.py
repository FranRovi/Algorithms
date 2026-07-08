# Leet Code Algo 1288. Removed Covered Intervals

def removeCoveredIntervals(intervals):
    sorted_intervals = sorted(intervals)
    hash_idx = {}
    len_intervals = len(intervals)
    
    for i in range(len_intervals):
        for j in range(i+1, len_intervals):
            if j in hash_idx:
                continue
            elif sorted_intervals[j][0] == sorted_intervals[i][0] and sorted_intervals[j][1] > sorted_intervals[i][1]:
                    if j not in hash_idx:
                        hash_idx[i] = 1
            elif sorted_intervals[j][0] >= sorted_intervals[i][0] and sorted_intervals[j][1] <= sorted_intervals[i][1]:
                    if j not in hash_idx:
                        hash_idx[j] = 1
    return len_intervals - len(hash_idx)

print(removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(removeCoveredIntervals([[1,4],[2,3]]))
print(removeCoveredIntervals([[1,4],[1,3],[5,8]]))
print(removeCoveredIntervals([[1,4],[3,6],[2,8],[1,9]]))
print(removeCoveredIntervals([[7,10],[5,15],[1,5]]))
print(removeCoveredIntervals([[5,10],[7,15],[1,5],[5,15]]))
