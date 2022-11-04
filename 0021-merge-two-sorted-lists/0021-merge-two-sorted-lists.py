# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        dummy_node = ListNode()
        tail = dummy_node
        
        
        while l1 != None and l2 != None:
            
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next 
            
        if l1 == None:
            tail.next = l2
        elif l2 == None:
            tail.next = l1
                
        return dummy_node.next
                
        