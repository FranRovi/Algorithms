# Leet Code Algo 1762. Buildings With An Ocean View

class Stack:
    def __init__(self):
        self.body = []
        self.count = 0
        self.max_val = 0

    def push(self, ele):
        if self.max_val < ele:
            self.max_val = ele
            self.count = 1
            self.body = [ele]
        else:
            self.body.append(ele)
            self.count += 1
    
    def pop(self):
        self.body.pop()
        self.count -= 1
    
    def peek(self):
        return self.body[self.count-1] 


def findBuildings(heights):
    my_stack = Stack()
    if len(heights) == 1:
        return [0]
    answer = []
    for i in range(len(heights)):
        if my_stack.count == 0:
            my_stack.push(heights[i])
        else:
            temp = my_stack.peek()
            if heights[i] < temp:
                my_stack.push(heights[i])
            else:
                while heights[i] >= temp:
                    my_stack.pop()
                    if my_stack.count == 0:
                        my_stack.max_val = 0
                        break
                    temp = my_stack.peek()
                my_stack.push(heights[i])
    hash_heights = {}
    for j in range(len(heights)):
        hash_heights[heights[j]] = j        
    for k in range(len(my_stack.body)):
        answer.append(hash_heights[my_stack.body[k]])       
    return answer
    
print(findBuildings([4,2,3,1]))
print(findBuildings([4,3,2,1]))
print(findBuildings([1,3,2,4]))