# Leet Code Algo 346. Moving Average from Data Stream

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.values = []
        self.counter = 0
        
    def next(self, val: int) -> float:
        self.values.append(val)
        self.counter += 1
        
        if self.counter < self.size:
            print(sum(self.values)/ self.counter)
            return sum(self.values)/ self.counter
        else:
            print(sum(self.values[self.counter-self.size:])/ self.size)
            return sum(self.values[self.counter-self.size:])/ self.size

movAvg_1 = MovingAverage(3)
movAvg_1.next(1)
movAvg_1.next(10)
movAvg_1.next(3)
movAvg_1.next(5)
