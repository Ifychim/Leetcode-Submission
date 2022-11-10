class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}
        
        for idx,num in enumerate(nums):
            compliment = target - num

        
            if compliment in nums_dict:
                return[nums.index(compliment),idx]
            
            nums_dict[num] = compliment
            
            
            
            