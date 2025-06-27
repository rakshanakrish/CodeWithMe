class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.append(value)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack underflow"
    
    def is_empty(self):
        return len(self.stack)==0
    
def balance(input1):
    s=Stack()
    input=input1.replace()
    for i in input:
        s.push(i)
    rev_str=""
    while not s.is_empty():
        rev_str+=s.pop()
    return rev_str

input="([x+y])"
output=r(input)
print(output)
