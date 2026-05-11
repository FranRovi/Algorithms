# Leet Code Algo 1396. Design Underground System.

class UndergroundSystem:
    def __init__(self):
        self.travels = {}
        self.times = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travels[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_sta = self.travels[id][0]
        start_time = self.travels[id][1]

        if start_sta + "-" + stationName not in self.times:
            self.times[start_sta + "-" + stationName] = [t - start_time]
        else:
            self.times[start_sta + "-" + stationName].append(t - start_time)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        num_of_travels = len(self.times[startStation + "-" + endStation])
        total_time_travels = sum(self.times[startStation + "-" + endStation]) 
        return total_time_travels / num_of_travels        
    
