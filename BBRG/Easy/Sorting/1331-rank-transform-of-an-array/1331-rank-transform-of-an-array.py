class Solution: #Sorting
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        sorted_arr = sorted(arr)
        ranking_dict = {}
        result = []
        rank = 1
        
        for num in sorted_arr:
            if num in ranking_dict:
                continue
            else:
                ranking_dict[num] = rank
                rank += 1
            
        for num in arr:
            
            if num in ranking_dict:
                result.append(ranking_dict[num])
                
        return result
        
        