# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_head, l2_head = l1, l2
        result = ListNode()
        
        res = result #we return res.next at end and it should be the LL's sum
        
        carry = 0
        
        while l1_head or l2_head or carry > 0:
            
            if l1_head:
                val_1 = l1_head.val
            else:
                val_1 = 0
            
            if l2_head:
                val_2 = l2_head.val
            else:
                val_2 = 0
            
            summation = val_1 + val_2 + carry
            
            carry = math.floor(summation/10) #carry is sum div 10
            summation = (summation%10) #add remainder to current node
        
            new_node = ListNode(val = summation)
            res.next = new_node
            
           
            res = res.next
            
            if l1_head:
                l1_head = l1_head.next
                
            if l2_head:
                l2_head = l2_head.next
            
        return result.next