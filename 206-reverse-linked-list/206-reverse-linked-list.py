# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = None
        
        curr = head
        
        while curr != None:
            
            temp = curr.next
            curr.next = result
            
            result = curr
            curr = temp
        
        
        
        return result