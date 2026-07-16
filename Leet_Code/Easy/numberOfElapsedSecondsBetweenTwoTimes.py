# Leet Code Algo 3986. Number of Elapsed Seconds Between Two Times.

def secondsBetweenTimes(startTime, endTime):
    start_time_sec = int(startTime[6:]) 
    end_time_sec = int(endTime[6:]) 
    start_time_min = int(startTime[3:5]) 
    end_time_min = int(endTime[3:5]) 
    start_time_hr = int(startTime[:2]) 
    end_time_hr = int(endTime[:2])

    total_seconds = (end_time_sec - start_time_sec + ((end_time_min - start_time_min) * 60) +
        ((end_time_hr - start_time_hr) * 3600)) 
    return total_seconds

print(secondsBetweenTimes("01:00:00", "01:00:25"))
print(secondsBetweenTimes("12:34:56", "13:00:00"))
