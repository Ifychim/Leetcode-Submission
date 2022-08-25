class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        
        for num in nums1:
            if num in nums2:
                result.append(num)
                
                #handle adding duplicate elements we have already seen
                num_idx = nums2.index(num)
                
                nums2.pop(num_idx)
            
        return result