class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        fast = 0 #keeps track of non-zeros elements
        slow = 0 #keeps track of zero elements
        
        while fast < len(nums):
            
            if nums[fast] != 0:
                #swap
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                
                slow += 1
            
            fast += 1
        return nums
            
        