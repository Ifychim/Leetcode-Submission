class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = set()
        nums_1 = set(nums1)
        
        for num in nums2:
            
            if num in nums_1:
                result.add(num)
                
        
        return result