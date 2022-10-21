class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        low = float(inf)
        high = 0
        result = 0
        
        while high < len(prices):
            
            #if we find a new low, update  sales
            if prices[high] < low:
                low = prices[high]
            else:
                result = max(prices[high]-low, result)
            
            high += 1
            
        return result