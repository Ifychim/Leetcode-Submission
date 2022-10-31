class OrderedStream:

    def __init__(self, n: int):
        
        #our stream should be able to hold n values n+1 since arrays are 0-based
        self.stream = [0]*(n+1)
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        #inserts pair into stream
        self.stream[idKey-1] = value
        
        chunk = []
        #returns largest chunk(longest consecutive idx holding values)

        while self.stream[self.ptr] != 0:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1
        
        print(chunk)   
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)