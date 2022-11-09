import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #we can find the kth largest number by storing the input in a min-heap
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        

    def add(self, val: int) -> int:
        
        #Add new incoming element to heap and
        heapq.heappush(self.heap, val)
    
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)