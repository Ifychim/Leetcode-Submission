class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        low = 0
        high = len(needle) - 1
        
        if high > len(haystack):
            return -1
        
        while high < len(haystack):
            
            subArr = haystack[low:high+1]
            
            if subArr == needle:
                return low
            else:
                low += 1
                high += 1
                
        return -1
        
        