class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        low = float(inf)
        high = 0
        max_profit = 0
        
        while high < len(prices):
            
            #if we find a new low, update lowest buying point
            if prices[high] < low:
                low = prices[high]
            else:
                max_profit = max(prices[high]-low, max_profit)
            
            high += 1
            
        return max_profit