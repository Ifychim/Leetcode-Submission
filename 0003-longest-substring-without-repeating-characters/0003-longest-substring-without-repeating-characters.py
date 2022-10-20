class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        
        longest = set()
        
        slow = 0
        fast = 0
        result = 0
        
        while fast < len(s):
            
            while s[fast] in longest:
                longest.remove(s[slow])
                slow += 1
                
            longest.add(s[fast]) 
            result = max(len(longest),result)
            fast += 1
            
           
        return result