class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return False
        
        num_map = {}
        
        for num in nums:

            num_map[num] = num_map.get(num, 0) + 1
            
            if num_map[num] > 1:
                return True
        return False
        