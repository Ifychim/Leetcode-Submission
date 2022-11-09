import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1: return stones[0]
        #intuition is to create a max heap of stones
        max_stones = []
        heapq.heapify(max_stones)
        for i in range(len(stones)):
            heapq.heappush(max_stones, stones[i] * -1)
            
            
        #continually pop from heap as long as we have more than 1 element
        while len(max_stones) > 1:
            y = heapq.heappop(max_stones)
            x = heapq.heappop(max_stones)
            
            if x == y:
                heapq.heappush(max_stones, 0)
            else:
                new_stone = abs(y-x)
                heapq.heappush(max_stones, new_stone * -1)
        
        
        return abs(max_stones[0])
        