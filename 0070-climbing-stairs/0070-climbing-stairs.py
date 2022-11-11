class Solution:
    def climbStairs(self, n: int) -> int:
        
        one, two = 1,1
        
        for i in range(0, n-1):
            #adding two previous values and getting new result
            temp = one
            one = one + two
            two = temp
            
        return one