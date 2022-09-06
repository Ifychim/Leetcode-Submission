class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1: return stones[0]
        
        stones.sort(reverse=True)
        
        low = 0
        high = 1
        
        while high < len(stones):
            
            if stones[low] == stones[high]:
                stones.pop(0)
                stones.pop(0)
            elif stones[high] != stones[low]:
                
                new_stone = stones[low] - stones[high]
                stones.pop(0)
                stones.pop(0)
                stones.insert(0,new_stone)
              
                stones.sort(reverse=True)
                
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
                