class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(0,n):
            nums1[(len(nums1)-n) + i] = nums2[i]
            
        #in-place sorting of nums1
        return nums1.sort()
     
    