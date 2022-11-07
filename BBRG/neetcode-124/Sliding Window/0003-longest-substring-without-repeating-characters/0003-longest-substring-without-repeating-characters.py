class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #brute force would be to find every possible substring and check for duplicates
        #O(n^2) O(n) space
        
#we have a window that expands constantly on the right side and a set to keep track of duplicates
#once a duplicate is encounterd, we remove characters from left side until duplicate is no longer in set O(n) time and Space
        
        low = 0
        high = 0
        substr_set = set()
        max_len = 0
        
        while high < len(s):
            
            #check if charcter is in set
            while s[high] in substr_set:
                substr_set.remove(s[low])
                low += 1
                
            substr_set.add(s[high])
            high += 1
            max_len = max(max_len, len(substr_set))
            
        return max_len
            
            

