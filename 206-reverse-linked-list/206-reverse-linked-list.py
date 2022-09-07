# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #O(N) time, O(1) space
        if head == None:
            return head
        
        prev = None
        curr = head
        
        #Change the pointers to point the opposite way
        while curr != None:
            
            curr_next_temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = curr_next_temp
            
            
        return prev
        
       
        
        