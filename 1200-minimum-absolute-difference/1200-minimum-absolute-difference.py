class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        result = []
        arr = sorted(arr)
        min_diff = float('inf')
        
        #find global min diff
        for i in range(0,len(arr)-1):
            min_diff = min(abs(arr[i+1] - arr[i]), min_diff)
        
        #find all pairs that have global min diff
        for i in range(0,len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff == min_diff:
                result.append([min([arr[i],arr[i+1]]), max([arr[i],arr[i+1]])])
                    
        return sorted(result)