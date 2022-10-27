class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq_map = {}
        
        for char in s:
            freq_map[char] = freq_map.get(char,0) + 1
        
        for k,v in freq_map.items():
            
            if v == 1:
                return s.index(k)
            
        return -1