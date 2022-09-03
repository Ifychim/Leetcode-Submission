class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #O(N) time, O(N) Space
        #convert uppercase to lower case
        new_str = ""
        s = s.lower()
        s = s.strip()
        
        #remove non-alphanumeric characters (spaces, e.t.c)
        for i in range(0,len(s)):
            if s[i].isalnum():
                new_str += s[i]
                
        low = 0
        high = len(new_str)-1
        
        while low <= high:
            if new_str[low] != new_str[high]:
                return False
            low += 1
            high -= 1
        return True
        