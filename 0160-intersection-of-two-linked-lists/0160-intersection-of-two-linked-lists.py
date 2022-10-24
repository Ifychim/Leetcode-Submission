# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr = headA
        mem_locs = set()
        
        while curr != None:
            mem_locs.add(hex(id(curr)))
            curr = curr.next
        
        curr = headB
        
        while curr != None:
            loc = hex(id(curr))
            if loc in mem_locs:
                return curr
            else:
                curr = curr.next
     