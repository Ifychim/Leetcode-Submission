class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        t_dict = {}
        s_dict = {}
        
        for char in t:
            t_dict[char] = 1 + t_dict.get(char,0)
            
        for char in s:
            s_dict[char] = 1 + s_dict.get(char,0)
            
        if s_dict == t_dict:
            return True
        else:
            return False
        