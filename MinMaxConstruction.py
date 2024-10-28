# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max = []#this is a tuple
        
    def peek(self):
        # Write your code here.
        if self.stack:
            return self.stack[-1]
        return None
    

    def pop(self):
        # Write your code here.
        if self.stack:
            self.min_max.pop()
            return self.stack.pop()
        return None
    

    def push(self, number):
        # Write your code here.
        self.stack.append(number)
        if self.min_max:
            curr_min = min(number,self.min_max[-1][0])
            curr_max = max(number,self.min_max[-1][1])
        else:
            curr_min=curr_max=number
        self.min_max.append((curr_min,curr_max))

    def getMin(self):
        # Write your code here.
        if self.min_max:
            return self.min_max[-1][0]

    def getMax(self):
        # Write your code here.
        if self.min_max:
            return self.min_max[-1][1]
        
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
  
