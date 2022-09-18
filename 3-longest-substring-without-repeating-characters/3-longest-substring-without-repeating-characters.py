class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        slow = 0
        substr = set()
        result = 0
        for fast in range(0,len(s)):
            
            
            #checks for a duplicate in our set
            while s[fast] in substr:
                substr.remove(s[slow])
                slow += 1
                
                
            
            substr.add(s[fast])
            result = max(len(substr), result)
        print(substr)
        return result