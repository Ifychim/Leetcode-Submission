class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0: return False
        
        palin = ""
        for char in s:
            
            if char.isalnum():
                
                palin += char.lower()
        
        low = 0
        high = len(palin) - 1
        
        while low <= high:
            
            if palin[low] != palin[high]: return False
            low += 1
            high -= 1
            
        return True