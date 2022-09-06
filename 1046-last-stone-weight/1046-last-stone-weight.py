class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1: return stones[0]
        
        stones.sort(reverse=True)
        
        smaller = 1
        bigger = 0
        
        while smaller < len(stones):
            
            if stones[smaller] == stones[bigger]:
                stones.pop(0)
                stones.pop(0)
            elif stones[smaller] != stones[bigger]:
                
                new_stone = stones[bigger] - stones[smaller]
                stones.pop(0)
                stones.pop(0)
                stones.insert(0,new_stone)
              
                stones.sort(reverse=True)
                
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
                