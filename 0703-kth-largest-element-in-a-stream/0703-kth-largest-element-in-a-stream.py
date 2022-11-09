import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        temp = self.heap
        
        
        while len(temp) > self.k:
            heapq.heappop(temp)
        
        return temp[0]
        
        #return temp[len(temp)-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)