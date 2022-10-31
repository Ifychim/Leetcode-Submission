class OrderedStream:

    def __init__(self, n: int):
        
        #our stream should be able to hold n values 
        self.stream = [0]*(n)
        self.ptr = 0
       
    def insert(self, idKey: int, value: str) -> List[str]:
        
        #inserts pair into stream, since keys are from 1-n, we insert at position key-1
        self.stream[idKey-1] = value
        
        chunk = []
        
        #returns largest chunk(longest consecutive idxs holding a value)
        #iterate through stream (using ptr) and build chunk at indices that arent 0-based
        for i in range(self.ptr, len(self.stream)):
            if self.stream[self.ptr] != 0:
                chunk.append(self.stream[self.ptr])
                self.ptr += 1
        
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)