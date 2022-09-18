class Solution:
    def isValid(self, s: str) -> bool:
     
        closing_matches = {')': '(', 
                           '}': '{',
                           ']': '[',
                          }
        
        open_brackets = []
        
        for char in s:
            
            if char not in closing_matches:
                open_brackets.append(char)
            else:
                if len(open_brackets) > 0 and open_brackets[-1] == closing_matches[char]: 
                    open_brackets.pop()
                else:
                    return False
                
        if len(open_brackets) == 0:
            return True
        else:
            return False
