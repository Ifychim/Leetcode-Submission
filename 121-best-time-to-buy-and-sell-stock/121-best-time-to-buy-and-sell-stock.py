class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        low = float(inf)
        high = 0
        
        while high < len(prices):
            
            #buy low 
            if prices[high] < low:
                low = prices[high]
            else:
                #sell high
                max_profit = max(max_profit, prices[high] - low)
            high += 1
        
        return max_profit