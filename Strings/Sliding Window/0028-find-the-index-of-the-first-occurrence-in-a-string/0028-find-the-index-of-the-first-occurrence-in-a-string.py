class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        low = 0
        high = len(needle)-1
        
        while high < len(haystack):
            
            sub_str = haystack[low:high+1]
            
            if sub_str  == needle:
                return low
            else:
                low += 1
                high += 1
        
        return -1