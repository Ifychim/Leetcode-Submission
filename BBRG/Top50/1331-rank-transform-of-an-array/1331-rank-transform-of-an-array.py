class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        sorted_arr = sorted(arr, key = lambda x: x) #sort input in ascending order
        
        rankings = {} #key = element, val = ranking
        
        rank = 1
        
        #update our rankings map to reflect the ranking of each number in the input
        for num in sorted_arr:
            
            if num not in rankings:
                rankings[num] = rank
                rank += 1
            
        
        #replace rankings in original aray
        for i in range(0, len(arr)):
            
            arr[i] = rankings[arr[i]]
        

        return arr