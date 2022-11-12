class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq_dict = {}
        
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        
        
        for key,vals in freq_dict.items():
            if vals == 1:
                return s.index(key)
            
        return -1
            