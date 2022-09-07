class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #O(N) time, O(1) space
        low = 0
        high = len(needle) - 1
        
        while high < len(haystack):
            
            subArr = haystack[low:high+1]
            
            if subArr == needle:
                return low
            low += 1
            high += 1
            
        return -1
        
    '''
    #O(N) time, O(1) space
    class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        result = None
        
        try:
            result = haystack.index(needle)
        except:
            return -1
        
        return result 
    '''