class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        first = m-1 #we compare pointer with incoming pointer
        second = n-1 #we compare incoming pointer with compare pointer
        filler = m+n-1 #we fill whichever element is greater between the two
        
        #iterate first array backwards
        for i in range(filler, -1, -1):
             
            #done iterating through second array
            if second < 0:
                break
            
            if nums2[second] > nums1[first]:
                nums1[i] = nums2[second]
                second -= 1
            else:
                nums1[i] = nums1[first]
                first -= 1
        
#if we dont finish going through the second array, we need to add the missing elements to the first array
        if second >= 0:
            nums1[:second+1] = nums2[:second+1]
            
        return nums1
        