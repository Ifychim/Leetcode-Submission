class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        cost_diff = []
        result = 0
        for c_a, c_b in costs:
            
            diff = c_b - c_a
            
            cost_diff.append([diff, c_a, c_b])
            
        cost_diff.sort()
        
        for i in range(0,len(cost_diff)):
            
            if i < len(cost_diff)//2:
                result += cost_diff[i][2]
            else:
                result += cost_diff[i][1]
                
        return result
        