# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #we can do this in O(n) space by using a set
        nodes = set() #set will store memory address of each node
        
        curr = head
        
        while curr != None:
            
            if hex(id(curr)) in nodes:
                return True
            else:
                nodes.add(hex(id(curr)))
                curr = curr.next
                
                
        return False