class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) < 2: return s
        stack = []
        stack.append(s[0])
        
        #we add to stack if curr char is not the same as the top of our stack 
        
        for i in range(1,len(s)):
            
            curr_char = s[i] 
            
            if stack and stack[-1] == curr_char:
                stack.pop()
            else:
                stack.append(curr_char)
          
        return ''.join(stack)
                