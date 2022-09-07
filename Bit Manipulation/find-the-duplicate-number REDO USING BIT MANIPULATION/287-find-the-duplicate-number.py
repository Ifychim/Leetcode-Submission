class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        duplicate_map = {}
        
        for num in nums:
            
            duplicate_map[num] = 1 + duplicate_map.get(num, 0)
        
        for key, val in duplicate_map.items():
            if val > 1:
                return key
        