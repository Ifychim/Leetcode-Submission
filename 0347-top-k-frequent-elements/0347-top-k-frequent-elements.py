class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #if we have a count of each element, we can return the top K elements
        
        freq_map = {}
        
        for n in nums:
            freq_map[n] = freq_map.get(n,0) + 1
            
        sorted_freq = sorted(freq_map.items(), key = lambda x: -x[1])
        
        result = []
        
        for i in range(0,k):
            
            result.append(sorted_freq[i][0])
            
        return result