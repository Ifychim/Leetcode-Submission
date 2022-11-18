from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.stream = deque()

    def next(self, val: int) -> float:
        self.stream.append(val)
        
        if len(self.stream) > self.size:
            self.stream.popleft()
        
        return sum(self.stream)/len(self.stream)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)