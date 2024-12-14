# Leet Code Algo 1603. Design Parking System

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        self.counterBig = 0
        self.counterMedium = 0
        self.counterSmall = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > self.counterBig:
                self.counterBig += 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > self.counterMedium:
                self.counterMedium += 1
                return True
            else:
                return False
        else:
            if self.small > self.counterSmall:
                self.counterSmall += 1
                return True
            else:
                return False

