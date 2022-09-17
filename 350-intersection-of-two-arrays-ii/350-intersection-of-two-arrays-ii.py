class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #O(N) time complexity, O(N) Space complexity
        
        nums1_map = {}
        result = []
        
        for num in nums1:
            nums1_map[num] = 1 + nums1_map.get(num,0)
        
        for num in nums2:
            try:
                val = nums1_map[num]
                
                if val > 0:
                    result.append(num)

                nums1_map[num] -= 1
            
            except:
                continue
        
        return result
    
    
        '''
        O(N^2) time complexity, O(N) Space complexity
        result = []
        
        for num in nums1:
            if num in nums2:
                result.append(num)
                
                #handle adding duplicate elements we have already seen
                num_idx = nums2.index(num)
                
                nums2.pop(num_idx)
            
        return result
        '''