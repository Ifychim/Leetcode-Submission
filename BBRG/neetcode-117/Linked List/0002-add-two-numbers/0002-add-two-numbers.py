# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        
        l1_ptr, l2_ptr, res_ptr = l1, l2, result
        
        carry = 0
        while l1_ptr != None or l2_ptr != None or carry: #dont know how to handle carry yet
            
            v1, v2 = 0, 0
            
            if l1_ptr != None:
                v1 = l1_ptr.val
            else:
                v1 = 0
                
            if l2_ptr != None:
                v2 = l2_ptr.val
            else:
                v2 = 0
                
            addition = v1 + v2 + carry
            carry = addition // 10
            addition = addition % 10
            
            new_node = ListNode(val = addition)
            res_ptr.next = new_node
            
            if l1_ptr != None:
                l1_ptr = l1_ptr.next
            else:
                l1_ptr = None
                
            if l2_ptr != None:
                l2_ptr = l2_ptr.next
            else:
                l2_ptr = None
                
            res_ptr = res_ptr.next
            
        return result.next
            