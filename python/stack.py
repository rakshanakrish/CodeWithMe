"""from collections import deque
stack=deque()
stack.append(20)
stack.append(10)
stack.append(1)
print(stack)"""

class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.append(value)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack overflow"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "empty stack"
    def is_empty(self):
        return len(self.stack)==0

s=Stack()
s.push(5)
s.push(10)
print(s.pop())
print(s.peek())