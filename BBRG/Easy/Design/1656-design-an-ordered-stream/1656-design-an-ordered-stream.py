class OrderedStream:

    def __init__(self, n: int):
        
        #n+1 to ensure our streams can take n values
        self.arr = [0]*(n+5)
        self.idx = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        #insert k,v pair into stream
        self.arr[idKey-1] = [idKey,value]
        
        #find largest possible chunk of inserted values starting from first position
        chunk = []
        
        while(self.arr[self.idx] != 0):
            chunk.append(self.arr[self.idx][1])
            self.idx += 1 
     
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)