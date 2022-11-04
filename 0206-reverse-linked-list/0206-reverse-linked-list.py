# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #reversing a singly-linked list means to reverse the current 
        #directions which nodes are pointing to. we can do so by updating prev and curr pointers
        
        #1->2->3->4->5->None (goes to)  None<-1<-2<-3<-4<-5
        
        prev = None
        curr = head
        
        while curr != None:
            
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
            
        #prev will be pointing to the new reversed head    
        return prev