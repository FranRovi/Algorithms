# Leet Code Algo 3834. Merge Adjacent Equal Elements.

class Stack:
        def __init__(self):
            self.stack = []

        def push(self, element):
            self.stack.append(element)

        def peek(self):
            if self.size() > 0:
                return self.stack[-1]

        def size(self):
            return len(self.stack)
        
        def update(self, val):
            self.stack[-1] += val
            self.checkPrevious()
        
        def checkPrevious(self):
            idx = len(self.stack) - 1
            while True and idx > 0:
                if self.stack[idx] == self.stack[idx - 1]:
                    temp = self.stack[idx]
                    self.stack.pop()
                    self.update(temp)
                    idx -= 1
                return
                        
        def returnValues(self):
            values = []
            for v in self.stack:
                values.append(v)
            return values
    
def mergeAdjacent(nums):
    myStack = Stack()
    myStack.push(nums[0])
    idx = 1
    while idx < len(nums):
        if nums[idx] == myStack.peek():
            myStack.update(nums[idx])
        else:
            myStack.push(nums[idx])
        idx += 1
    return myStack.returnValues()


print(mergeAdjacent([3,1,1,2]))
print(mergeAdjacent([2,2,4]))
print(mergeAdjacent([3,7,5]))
print(mergeAdjacent([4,2,2]))
print(mergeAdjacent([4,2,1,1]))