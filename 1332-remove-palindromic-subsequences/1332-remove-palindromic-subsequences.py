class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        #if the given string is a palindrome, we can remove it in a single step
        if s == s[::-1]: return 1
        
        else:
            return 2
        