class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        result = None
        
        try:
            result = haystack.index(needle)
        except:
            return -1
        
        return result
        
        