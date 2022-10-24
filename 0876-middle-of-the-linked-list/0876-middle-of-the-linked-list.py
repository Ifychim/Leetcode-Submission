# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first_count = 0
        second_count = 0
        curr = head
        
        while curr != None:
            
            curr = curr.next
            first_count += 1
        
        curr = head
        first_count = math.floor(first_count/2)
        
        while curr != None:
            
            if second_count == first_count:
                return curr
            curr = curr.next
            second_count += 1