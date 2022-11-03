class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        arithmetic_stack = []
        
        for char in tokens:
            
            if char == "+":
                val2, val1 = arithmetic_stack.pop(), arithmetic_stack.pop()
                res = val1 + val2
                
                arithmetic_stack.append(res)
                
            elif char == "-":
                val2, val1 = arithmetic_stack.pop(), arithmetic_stack.pop()
                res = val1 - val2
                arithmetic_stack.append(res)
                
            elif char == "*":
                val2, val1 = arithmetic_stack.pop(), arithmetic_stack.pop()
                res = val1 * val2
                arithmetic_stack.append(res)
                
            elif char == "/":
                val2, val1 = arithmetic_stack.pop(), arithmetic_stack.pop()
                res = int(val1/val2)
        
                arithmetic_stack.append(res)
            else:
                arithmetic_stack.append(int(char))
                
        return arithmetic_stack[0]
       
                
                    