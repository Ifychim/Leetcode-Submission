class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        result = -1
        
        try:
            if haystack.index(needle) > -1:
                result = haystack.index(needle)
        except:
            return -1
        
        return result
        
        