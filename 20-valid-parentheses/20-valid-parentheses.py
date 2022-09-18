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
                open_char = ""
                
                if len(open_brackets) > 0: open_char = open_brackets[-1]
                    
                closing_char = closing_matches[char]
                
                if closing_char == open_char:
                    open_brackets.pop()
                else:
                    return False
                
        if len(open_brackets) == 0:
            return True
        else:
            return False