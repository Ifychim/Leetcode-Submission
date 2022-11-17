class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #if we have two pointers, one to keep track of zero based elements, 
        #other to keep track on non-zeros. If non-zero != zero, then swap
        
        if len(nums) <= 1: return nums
        
        zeros = 0
        non_zeros = 0
        
        while non_zeros < len(nums):
                
            if nums[non_zeros] != 0:
                temp = nums[non_zeros]
                nums[non_zeros] = nums[zeros]
                nums[zeros] = temp
        
                zeros += 1
            
            non_zeros += 1
        
        return nums