class Solution:
    #memoization to store duplicate sub-problems
    def fib(self, n: int, memo = {}) -> int:
        
        #if key in memo, return
        if n in memo: 
            return memo[n]
        
        if n == 2 or n==1: return 1
        if n == 0: return 0
        memo[n] = self.fib(n-2, memo) + self.fib(n-1, memo)
        
        return memo[n]