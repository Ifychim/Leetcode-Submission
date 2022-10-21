class Solution: #Array
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        
        for i in range(0,len(operations)):
            op = operations[i]
            
            if op[0] == "+" or op[len(op)-1] == "+":
                result += 1
            else:
                result -= 1
                
        return result