# Leet Code Algo 1381. Design a Stack With Increment Operation

class CustomStack:

    def __init__(self, maxSize: int):
        self.limit = maxSize
        self.stack = []
        self.counter = 0

    def push(self, x: int) -> None:
        if self.counter < self.limit:
            self.stack.append(x)
            self.counter += 1
            # print(self.stack)
        return

    def pop(self) -> int:
        if self.counter <= 0:
            # print(-1)
            return -1
        else:
            popped_element = self.stack.pop()
            self.counter -= 1
            # print(self.stack, popped_element)
            return popped_element

    def increment(self, k: int, val: int) -> None:
        min_val = k if k < self.limit else self.limit
        for i in range(min_val):
            if i == self.counter:
                break
            self.stack[i] += val
        # print(self.stack)
        return
    
testOne = CustomStack(3)
testOne.push(1)
testOne.push(2)
testOne.pop()
testOne.push(2)
testOne.push(3)
testOne.push(4)
testOne.increment(5, 100)
testOne.increment(2, 100)
testOne.pop()
testOne.pop()
testOne.pop()
testOne.pop()

# print("*** --- ***")

testTwo = CustomStack(2)
testTwo.push(34)
testTwo.pop()
testTwo.increment(8, 100)
testTwo.pop()
testTwo.increment(9, 91)
testTwo.push(63)
testTwo.pop()
testTwo.push(84)
testTwo.increment(10, 93)
testTwo.increment(6, 45)
testTwo.increment(10, 4)