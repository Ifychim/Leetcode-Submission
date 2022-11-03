from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #brute force would be to create frequency dict of s1 
        #then iterate through s2 checking freq every substr of len(n) where n = len(s1). 
        #O(n^2) iteration and creating dict.
        
        s1_count = Counter(s1)
            
        for high in range(len(s2)):
            
            temp = Counter(s2[high:high+len(s1)])
            
            if temp == s1_count:
                return True
            else:
                high += 1
        
        
            