class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #brute force would be to have a nested for-loop and check all possible sums
        
        #A slightly better variation would be to sort input and use 2 pointers
        
        #Optimal would be to use a hash map to keep track of values & compliments
        #that way, if we have seen a compliment, we know that there are two nums == target
        
        compliment_map = {} #num:compliment
        
        for idx,num in enumerate(nums):
            
            compliment = target - num
            
            if compliment in compliment_map:
                return [nums.index(compliment),idx]
            else:
                compliment_map[num] = compliment
            