class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_low = float('inf')
        max_profit = 0
        
        for price in prices:
            
            if price <= buy_low:
                buy_low = price
            else:
                #Buy low, sell high.
                profit = price - buy_low
                max_profit = max(profit, max_profit)
                
        return max_profit