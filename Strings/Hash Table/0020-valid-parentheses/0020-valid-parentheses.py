class Solution:
    def isValid(self, s: str) -> bool:
         
        brackets = {')':'(', '}':'{', ']':'['}
        
        if len(s) % 2 != 0 or s[0] in brackets.keys():
            return False
        
        open_brackets = []

        for char in s:
            
            if char in brackets.values():
                open_brackets.append(char)
             
            else:
                if len(open_brackets) > 0 and open_brackets[-1] == brackets[char]:
                        open_brackets.pop()
                else:
                    return False
     
                

        if len(open_brackets) == 0:
            return True
        else:
            return False