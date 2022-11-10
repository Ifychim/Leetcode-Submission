import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #intuition is to have a mean heap of size K. 
        #Once that is achieved, the kth largest element will always be the root.
                
        heapq.heapify(nums) #O(n)
        
        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]
