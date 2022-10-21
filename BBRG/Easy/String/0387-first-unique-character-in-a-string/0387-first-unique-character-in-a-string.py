
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_dict = {}
        
        for char in s:
            char_dict[char] = char_dict.get(char,0) + 1
            
        for k,v in char_dict.items():
            
            if v == 1:
                return s.index(k)
        
        return -1
        