class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            #mid point is the distance between high and low pointers
            mid_point = (low + high) // 2
            
            if nums[mid_point] == target:
                return mid_point
            
            
            if nums[mid_point] < target:
                low = mid_point + 1
            elif nums[mid_point] > target:
                high = mid_point - 1
                
        return -1
                
        