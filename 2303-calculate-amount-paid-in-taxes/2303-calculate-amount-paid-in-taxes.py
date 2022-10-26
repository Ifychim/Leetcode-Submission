class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        #0-3, 3-7, 7-12
        
        result = 0
        #compute upper bound ranges
        
        ranges = {}
        start = 0
        
        for i in range(0,len(brackets)):
            
            upper, percent = brackets[i]
            
            ranges[i] = [start, upper]
            
            start = upper
        
        i = 0
        for r in ranges.values():
            
            lower, upper = r
            
            possible_dollars = upper - lower
            print(possible_dollars, income)
            if income > 0:
                if possible_dollars <= income:
                    result += possible_dollars * (brackets[i][1]/100)
                    income -= possible_dollars
                elif possible_dollars > income:
                    result += income * (brackets[i][1]/100)
                    income -= possible_dollars
                
            i+= 1
            
        return result
        