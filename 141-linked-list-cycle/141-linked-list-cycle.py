# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#O(N) time, O(1) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       
        #Edge Case -> Empty list or List with only one element
        if head == None or head.next == None : return False
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False