# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #O(n) time, O(n) space
        arr = []
        curr = head
        
        while curr != None:
            arr.append(curr)
            curr = curr.next
        
        return arr[math.floor(len(arr)/2)]
        
        