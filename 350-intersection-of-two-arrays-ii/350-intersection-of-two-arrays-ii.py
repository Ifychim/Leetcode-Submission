class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        for num in nums1:
            
            if num in nums2:
                result.append(num)
                
                num2_idx = nums2.index(num)
                nums2.pop(num2_idx)
            
                
        return result