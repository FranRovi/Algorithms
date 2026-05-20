# Leet Code Algo 1756. Design Most Recently Used Queue

class MRUQueue:

    def __init__(self, n: int):
        self.nums = []
        for i in range(1, n+1):
            self.nums.append(i)
        

    def fetch(self, k: int) -> int:
        temp = self.nums[k-1]
        self.nums = self.nums[:k-1] + self.nums[k:]
        self.nums.append(temp)
        return temp

    
testOne = MRUQueue(8)
print(testOne.fetch(3))
print(testOne.fetch(5))
print(testOne.fetch(2))
print(testOne.fetch(8))

print("*** --- ***")

testTwo = MRUQueue(3)
print(testTwo.fetch(2))
print(testTwo.fetch(1))
print(testTwo.fetch(2))
print(testTwo.fetch(2))
print(testTwo.fetch(2))
print(testTwo.fetch(3))
print(testTwo.fetch(2))
print(testTwo.fetch(1))
print(testTwo.fetch(1))
print(testTwo.fetch(2))