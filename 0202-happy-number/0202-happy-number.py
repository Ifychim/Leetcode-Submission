class Solution:
    def isHappy(self, n: int) -> bool:
        
        res = 0
        if n==1:
            return True
        if n==4:
            return False
        for i in str(n):
            res += int(i) * int(i)
        n = res
        
        return Solution.isHappy(self,n)