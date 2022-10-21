class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #merge then sort
        
        for i in range(0,n):
            nums1[i+m] = nums2[i]
            
        
        return nums1.sort()
    
                    
                