class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        result = 0
        
        optimal_costs = []
        #decide at each step whether cityB cost or cityA cost is cheaper. 
        #cityB - cityA -> if > 0 then A is cheaper, if < 0 b is cheaper
        
        for aCost,bCost in costs:
            
            cost_diff = bCost - aCost
            
            optimal_costs.append([cost_diff, aCost, bCost])
            
#once we have our optimal costs, we can then sort it in increasing order by cost_diff and send the first half to b and the other half to A 
        
        optimal_costs = sorted(optimal_costs, key=lambda x: x[0])
        half = len(optimal_costs) // 2
        
        for i in range(0,len(optimal_costs)):
            
            opt_cost, cityA_cost, cityB_cost = optimal_costs[i]
            
            if i < half:
                result += cityB_cost
            else:
                result += cityA_cost
                
        return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        