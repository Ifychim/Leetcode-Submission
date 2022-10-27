class Solution:
    def countDistinct(self, s: str) -> int:
        
        res = set()
        
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                
                sub_str = s[i:j+1]
               
                res.add(sub_str)
                
        return len(res)