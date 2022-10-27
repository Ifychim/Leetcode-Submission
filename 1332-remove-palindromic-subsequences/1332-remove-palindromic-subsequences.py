class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
    #if the given string is a palindrome, then we can remove it in one step. 
        if s[::-1] == s:
            return 1
    #if the string is not a palindrome, we will always need only 2 steps -> 1 - remove all b's, 2 - remove all a's
        else:
            return 2
        
      