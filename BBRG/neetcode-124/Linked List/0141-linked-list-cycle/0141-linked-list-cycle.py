# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #the below solution can be improved by having two pointers (slow,fast)
        #we know that if something is moving twice as fast then it is bound to cross paths.
        if head == None:
            return False
        slow, fast = head,head
        
        #even vs odd check
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            

            
            
        return False
        '''
        #we can do this in O(n) time & space by using a set.
        nodes = set() #set will store memory address of each node
        
        curr = head
        
        while curr != None:
            
            if hex(id(curr)) in nodes:
                return True
            else:
                nodes.add(hex(id(curr)))
                curr = curr.next
            
        return False
        '''