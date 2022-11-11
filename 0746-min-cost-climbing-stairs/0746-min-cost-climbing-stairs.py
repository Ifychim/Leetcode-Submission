class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        
        
    #iterate in reverse order from n-3 and compute new cost depending on idx. min( idx[i] = idx[i] + idx[i+1]
    #                                                                              idx[i] = idx[i] + idx[i+2])
        
        
        for i in range(len(cost)-3, -1, -1):
            single_jump = cost[i] + cost[i+1]
            double_jump = cost[i] + cost[i+2]
            
            cost[i] = min(single_jump,double_jump)
            
        #return the min starting from either position 0 or position 1
        return min(cost[0], cost[1])