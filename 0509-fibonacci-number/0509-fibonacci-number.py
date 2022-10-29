
class Solution:
    #memoization to store duplicate sub-problems
    def fib(self, n: int ) -> int:
        memo = {}
        #if key in memo, return
        if n in memo: 
            return memo[n]
        
        if n == 2 or n==1: return 1
        if n == 0: return 0
        
        #store each recursive call in dictionary
        memo[n] = self.fib(n-2) + self.fib(n-1)
        
        print(memo)
        return memo[n]