class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = 0
        high = 0
        max_profit = 0
        
        while high < len(prices):
            
            if prices[high] < prices[low]:
                low = high
             
            else:
                sell = prices[high]-prices[low]
                max_profit = max(max_profit, sell)
            
            
            high += 1
            
        return max_profit