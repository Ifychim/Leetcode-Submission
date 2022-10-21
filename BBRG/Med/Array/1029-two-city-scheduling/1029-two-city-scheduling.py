class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #idea is to find the "n" cheapest B flights and the "n" cheapest A flights
        
        cost_diff = []
        result = 0
        
        #find the difference in costs (b-a) if negative then b is cheaper
        for c_a, c_b in costs:
            
            diff = c_b - c_a
            
            cost_diff.append([diff, c_a, c_b])
        
        #sorting is necessary in order to find the "cheapest flights"
        cost_diff.sort()
        
        #add the "n" cheapest b flights, to result then the "n" cheapest A flights to result
        for i in range(0,len(cost_diff)):
            
            #
            if i < len(cost_diff)//2:
                result += cost_diff[i][2]
            else:
                result += cost_diff[i][1]
                
        return result
        