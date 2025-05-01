# Leet Code Algo 252. Meeting Rooms

def canAttendMeetings(intervals):
    sorted_intervals = sorted(intervals)
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
            return False
    return True

print(canAttendMeetings([[0,30],[5,10],[15,20]]))
print(canAttendMeetings([[7,10],[2,4]]))