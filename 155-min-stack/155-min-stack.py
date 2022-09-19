class MinStack:
    
    def __init__(self):
        self.stack = []
        
    
    def push(self, val:int) -> None:
        self.stack.append(val)
        
        
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[len(self.stack)-1]
    
    def getMin(self) -> int:
        self.minimum = float(inf)
        
        for num in self.stack:
            
            if num < self.minimum:
                self.minimum = num
                
        return self.minimum
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()