class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1: return len(s)
        
        left = 0 
        right = 0
        res = 0
        
        substr_set = set()
        
        while right < len(s):
        
            #if after adding a char to our set we encounter a duplicate, shrink window from left
            while s[right] in substr_set:
                substr_set.remove(s[left])
                left += 1
                
            substr_set.add(s[right])
            res = max(res, len(substr_set))
            
            right += 1
            
        return res
            
        