class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        #find how much cheaper it is to send to city b than city a
        cheapest = []
        
        for cost in costs:
            city_a, city_b = cost
            
            cost_diff = city_b - city_a
            
            cheapest.append([cost_diff, city_a, city_b])
            
        #Now that we have the cost difference relative to city b,
        #After sorting, We can send the first N/2 people to city b then the rest          to city_a   
        cheapest.sort()
        result = 0
        half = len(cheapest)//2
        
        for i in range(0,len(cheapest)):
            
            if i < half:
                result += cheapest[i][2]
            else:
                result += cheapest[i][1]
                
        return result
            
        