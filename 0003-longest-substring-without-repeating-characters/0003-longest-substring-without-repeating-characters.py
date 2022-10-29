class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        end = 0
        sub_str = set()
        result = 0
        
        #Window which adds the characters in a sequential manner to our sub_str set
        #Once we encounter a duplicate, we remove elements from the left 
        #until duplicate character does not exist anymore
        
        while end < len(s):
            
            while s[end] in sub_str:
                sub_str.remove(s[start])
                start += 1
        
            sub_str.add(s[end])
            result = max(result,len(sub_str))
            
            end += 1
            
        return result