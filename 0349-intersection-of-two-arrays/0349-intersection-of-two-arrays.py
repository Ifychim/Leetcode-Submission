class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        nums_1 = set(nums1)
        
        for num in nums2:
            
            if num in nums_1:
                result.append(num)
                
        
        return set(result)