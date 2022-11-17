class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
          
        result = []
        nums.sort()

        #three pointers, current(i), left, right
        
        for i in range(0,len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]: continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:

                triplet_sum = nums[i] + nums[left] + nums[right]
    
                if triplet_sum == 0:
            
                    result.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[left] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                if triplet_sum < 0:
                    left += 1
                elif triplet_sum > 0:
                    right -= 1
            
        return result
            
            