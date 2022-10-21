class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num_dict = {}
        
        for num in nums:
            num_dict[num] = num_dict.get(num,0) + 1
            
        for k,v in num_dict.items():
            
            if v > len(nums) / 2:
                return k
            
        