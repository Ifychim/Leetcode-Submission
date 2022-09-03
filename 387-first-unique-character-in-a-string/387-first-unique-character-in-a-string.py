class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_dict = {}
        
        for char in s:
            char_dict[char] = 1 + char_dict.get(char, 0)
        
        for key,val in char_dict.items():
            
            if val == 1:
                
                return s.index(key)
        
        return -1