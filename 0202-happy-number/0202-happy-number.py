class Solution:
    def isHappy(self, n: int) -> bool:
        
        n_str = str(n)
        
        res = 0
        
        if n == 1:
            return True
        elif n ==2 or n==3 or n== 4:
            return False
        
        for i in range(0,len(n_str)):
            res += int(n_str[i]) * int(n_str[i])
         
        return self.isHappy(res)