class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        t_map, s_map = {}, {}
        
        for char in s:
            s_map[char] = s_map.get(char,0) + 1
            
        for char in t:
            t_map[char] = t_map.get(char,0) + 1
            
        
        if t_map == s_map:
            return True
        else:
            return False