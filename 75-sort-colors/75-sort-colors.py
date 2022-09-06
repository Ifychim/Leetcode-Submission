class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        curr = 0
        while curr <= high:
            if nums[curr] == 0:
                
                temp = nums[low]
                nums[low] = nums[curr]
                nums[curr] = temp
                
                low += 1
                curr += 1
                
            elif nums[curr] == 2:
                
                temp = nums[high]
                nums[high] = nums[curr]
                nums[curr] = temp
                
                high -= 1
            else:
                curr += 1
                
        return nums
    
    
    '''
    HARD CODED SOLUTION 
        zeros = []
        ones = []
        twos = []
        result = []
        
        for num in nums:
            if num == 0:
                zeros.append(num)
            elif num == 1:
                ones.append(num)
            else:
                twos.append(num)
                
        result.extend(zeros)
        result.extend(ones)
        result.extend(twos)
        nums.clear()
        nums.extend(result)
        
    '''
                