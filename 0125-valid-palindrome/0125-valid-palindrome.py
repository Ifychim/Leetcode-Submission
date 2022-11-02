class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ''
        
        s = s.lower()
        
        for char in s:
            
            if char.isalnum():
                res += char
                
        low,high = 0, len(res)-1
        
        while low <= high:
            if res[low] != res[high]:
                return False
            
            low += 1
            high -= 1
            
        return True