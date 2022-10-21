class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        low = 0
        
        for high in range(1,len(prices)):
            
            if prices[high] > prices[low]:
                sell = prices[high] - prices[low]
                max_profit = max(sell,max_profit)
                
            elif prices[high] < prices[low]:
                low = high
                
        return max_profit