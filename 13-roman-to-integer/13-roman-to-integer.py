class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_map = {}
        
        for symbol in s:
            if symbol == 'I':
                roman_map[symbol] = 1
            elif symbol == 'V':
                roman_map[symbol] = 5
            elif symbol == 'X':
                roman_map[symbol] = 10
            elif symbol == 'L':
                roman_map[symbol] = 50
            elif symbol == 'C':
                roman_map[symbol] = 100
            elif symbol == 'D':
                roman_map[symbol] = 500
            elif symbol == 'M':
                roman_map[symbol] = 1000
                
        if len(s) == 1: return roman_map[s]
        
        total = 0
        i = 0
     
        while i < len(s):
            
            #substration case
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:

                total += roman_map[s[i+1]] -  roman_map[s[i]]
                i += 2

            else:
                total += roman_map[s[i]]
                i += 1
              
            
        return total