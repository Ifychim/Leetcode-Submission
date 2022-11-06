# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #the idea is to have two pointers which are always n distance apart.
        #once the fast pointer hits the end of the list then we know the slow will be n from the end.
        #we need to use a dummy node because in order to delete the nth from the end we need to be at nth-1.
        
        dummy_node = ListNode(next = head)
        slow = dummy_node
        fast = head
        
        #moving our fast pointer to be 'n' distance apart
        for i in range(0,n):
            fast = fast.next
            
        
        while fast != None:
            slow = slow.next
            fast = fast.next

        #once fast has reached the end of the list, we update the pointers of nth-1        
        slow.next = slow.next.next
                
        
        return dummy_node.next