class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Most water = Maximum area. Area of a rectangle = l*h
        
        #brute force would be to compute all possible areas of the container O(n^2)
        
#this can be optimized to o(n) using two pointers. to compute area between two points
#atfter computing an area. we should always move the lower line inwards to guarantee max possible area
        left = 0
        right = len(height)-1
        
        max_area = 0
    
        while left <= right:
            
            length = right - left
            min_height = min(height[left], height[right])
            curr_area = length * min_height
            
            max_area = max(max_area, curr_area)
            
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
                
        return max_area