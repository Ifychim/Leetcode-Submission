#O(n) time complexity, O(1) space complexity solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
    
    # Compute all possible container sizes (areas) & return the max
    # Area (amount of water between two lines) = length (high-low) * width(max vertical line)
    
        max_container = 0
        low = 0
        high = len(height) - 1


        # Always move lower pointer, compute area, compare with max container
        while low <= high:

            length = high - low
            width = min(height[low], height[high])

            area = length * width

            max_container = max(area, max_container)

            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1

        return max_container

