# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = None
        curr = head
        
        while curr != None:
            
            temp = curr.next
            curr.next = newHead
           
            newHead = curr
            curr = temp
        
        return newHead
        