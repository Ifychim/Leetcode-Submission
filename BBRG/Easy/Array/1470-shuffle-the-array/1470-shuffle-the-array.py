import math
class Solution: #Array
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        x_arr = nums[0:n]
        y_arr = nums[n:]
        
        result = []
        
        for i in range(0, n):
            
            result.append(x_arr[i])
            result.append(y_arr[i])
            
        return result