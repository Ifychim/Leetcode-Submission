class OrderedStream:

    def __init__(self, n: int):
        self.stream = [0] * (n + 1)
        self.ptr = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.stream[idKey-1] = [idKey,value] #we need to offset by one since ids are 1 idxed
      
        res = []
        
        while self.stream[self.ptr] != 0:
            res.append(self.stream[self.ptr][1])
            self.ptr += 1
            
        return res
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)