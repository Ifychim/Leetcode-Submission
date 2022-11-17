class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0: return -1
        
        #find smallest index (modified binary search)
        left = 0
        right = len(nums) - 1

        
        while left < right:
            mid = (right + left) // 2
            
            #if mid point is greater than furthest element on the right, 
            #then we know smallest element is on the right hand side of rotated array
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
                
        
        #choose which side to search the array (left vs right of smallest idx)
        smallest = left
        left = 0
        right = len(nums)-1
        
        if nums[smallest] <= target and nums[right] >= target:
            left = smallest
        else:
            right = smallest
        
        #perform binary search on selected side
        
        while left <= right:
            
            mid = (right + left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
            
            
            
            
            
            