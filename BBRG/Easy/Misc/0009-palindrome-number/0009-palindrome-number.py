class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        str_num = str(x)
        if str_num[0] == "-": return False
    
        
        low = 0
        high = len(str_num)-1
        #print(str_num[high])
        
        while low <= high:
            
            if str_num[low] != str_num[high]:
                return False
            else:
                low += 1
                high -= 1
                
        return True
        
        