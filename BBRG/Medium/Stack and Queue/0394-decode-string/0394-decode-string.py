class Solution:
    #O(n) time & O(n) space
    def decodeString(self, s: str) -> str:
        stack = []
        
        #add chars in stack until we detect a closing bracket
        
        for char in s:
            
            if char != "]":
                stack.append(char)
                
            else:
                #pop chars from char & build substr until we detect an open bracket
                sub_str = ""
                
                while stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                    
                #pop opening bracket then process digit(k)
                stack.pop()
                
                k = ""
                
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    
                stack.append(int(k)*sub_str)
        
        res = "".join(stack)
        
        return res
                