class OrderedStream:

    def __init__(self, n: int):
        
        self.arr = [None]*(n+1)
        self.lastIdx = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.arr[idKey-1] = [idKey,value]
        chunk = []
        
        while(self.arr[self.lastIdx] != None):
            chunk.append(self.arr[self.lastIdx][1])
            self.lastIdx += 1 
            
        #print(chunk)     
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)