class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) == 1: return 1
        
        palin_map = {}
        chars = set(s)
        palin_check = set()
        result = 0
        
        for char in s:
            palin_map[char] = palin_map.get(char, 0) + 1
            
        for key,val in palin_map.items():
            
            if val % 2 != 0:
                palin_map[key] -= 1
            else:
                palin_check.add(key)
                
            
        result = sum(palin_map.values())
        
        for char in chars:
            if char not in palin_check:
                result += 1
                break
                
        return result
            
            