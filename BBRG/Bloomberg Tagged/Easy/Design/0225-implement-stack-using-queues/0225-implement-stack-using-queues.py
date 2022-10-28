class MyStack:
    
    def __init__(self):
        self.main_q = []
        
    def push(self, num: int) -> None:
        self.main_q.insert(len(self.main_q), num)
    
    def pop(self) -> int:
        top = self.main_q[len(self.main_q)-1]
        del self.main_q[len(self.main_q)-1]
        return top
    
    def top(self) -> object:
        return self.main_q[len(self.main_q)-1]
   
    
    def empty(self) -> bool:
        if len(self.main_q) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()