class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n != 1:
            
            n /= 3
            
            temp = str(n)
            temp = temp.split(".")
            if int(temp[1]) != 0:
                break
            
            
        if n == 1:
            return True
        else:
            return False