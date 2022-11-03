class Solution:
    def isValid(self, s: str) -> bool:
        
        closed_bracket_map = {"}":"{", ")":"(", "]": "["}
        
        open_bracket_stack = []
        
        
        for char in s:
            
            if char not in closed_bracket_map:
                
                open_bracket_stack.append(char)
                
            else:
                
                if len(open_bracket_stack) > 0 and closed_bracket_map[char] == open_bracket_stack[-1]:
                    
                    open_bracket_stack.pop()
                else:
                    return False
                
        
        if len(open_bracket_stack) == 0:
            return True
        else:
            return False
        
        
        