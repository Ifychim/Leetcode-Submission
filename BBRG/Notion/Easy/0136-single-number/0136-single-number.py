class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq_count = {}
        
        for num in nums:
            
            freq_count[num] = freq_count.get(num,0) + 1
            
        for k, v in freq_count.items():
            
            if v == 1:
                return k
            
        