class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        
        sum_dict = {}
        
        for i in range(0,len(nums)):
            compliment = target - nums[i]
            
            if compliment in sum_dict:
                return [nums.index(compliment), i]
            
            sum_dict[nums[i]] = compliment
            
        