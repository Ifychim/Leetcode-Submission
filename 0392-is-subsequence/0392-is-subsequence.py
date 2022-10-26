class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        #if len(s) > len(t): return False
        #elif len(s) == 0: return True
        
        t_ptr = 0
        s_ptr = 0
        
        #
        while t_ptr < len(t) and s_ptr < len(s):
            
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
                
            t_ptr += 1
        
        #if we successfully traversed through string S then we know it is a valid subsequence   
        if len(s) == s_ptr:
            return True
        else:
            return False
        