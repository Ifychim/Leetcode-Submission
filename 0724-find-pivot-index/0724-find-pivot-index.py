class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        for i in range(0,len(nums)):
            
            left = nums[:i]
            right = nums[i+1:]
            
            left_sum = 0
            right_sum = 0
            
            #if len(left) != 1:
            left_sum = sum(left)
                
            #if len(right) != 1:
            right_sum = sum(right)
                
            if left_sum == right_sum:
                print(left)
                print(right)
                return i
            
            
            
        return -1