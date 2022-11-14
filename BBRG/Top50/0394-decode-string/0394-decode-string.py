class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        result = ""
        for char in s:
            #append all characters which aren't closing brackets to our stack
            if char != "]":
                stack.append(char)
                
            else:
                #pop all characters until we encounter an opening bracket then process it
                sub_str = ""
                while stack and stack[-1] != "[":
                    
                    sub_str = stack.pop() + sub_str
                    
                #process k and opening bracket
                open_bracket = stack.pop()
                k = ""
                
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                k = int(k)
                
              #multiply the substr k times and then append it to our stack for future processing
                sub_str *= k
                stack.append(sub_str)
                
                
                
        return ''.join(stack)