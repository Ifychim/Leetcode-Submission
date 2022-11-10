from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        sub_str = Counter(s1)  
        
        for i in range(0, len(s2)):
            comparison = Counter(s2[i:i+len(s1)])
            
            if sub_str == comparison:
                return True
            
        return False
            