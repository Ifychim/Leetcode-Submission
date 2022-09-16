class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count frequency of each element in nums
        frequency = {}
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        
        #sort in descending order by frequency 
        sorted_frequency = sorted(frequency.items(), key = lambda x: -x[1])
    
        
        #return the k most frequent elements
        res = []
        for num in range(0,k):
            key, val = sorted_frequency[num]
            res.append(key)
            
        return res
        
