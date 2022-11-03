class MinStack:

    def __init__(self):
        self.stack = []
        self.globalMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.globalMin) > 0:
            self.globalMin.append(min(self.globalMin[-1], val))
        else:
            self.globalMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.globalMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.globalMin[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()