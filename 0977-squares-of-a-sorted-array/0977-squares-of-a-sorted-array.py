import heapq

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        #we can create a min-heap to store the squares of each num
        #we then need to pop each element from the min heap and return the result
        min_heap = []
        result = []
        
        for num in nums:
            
            square = abs(num * num)
            
            heapq.heappush(min_heap, square)
            
        while min_heap:
            
            result.append(heapq.heappop(min_heap))
            
        return result
            