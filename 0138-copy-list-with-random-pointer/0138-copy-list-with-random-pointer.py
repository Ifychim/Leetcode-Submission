"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #the idea is to map old nodes to a deep copy this can be done using a dict.
        #once this is done, we can go ahead and update the pointers of our newly created list
        
        old_to_new = {None:None} #key = curr_node in linked list (stores next & random pointers), val = new_node
                                 #Initialize as None, for edge case
        cur = head
        
        while cur != None:
            #create a copy of each node
            new_node = Node(cur.val)
            old_to_new[cur] = new_node 
            
            cur = cur.next
        
        #update pointers of newly created nodes
        
        cur = head
        while cur != None:
            new_node = old_to_new[cur]
            new_node.next = old_to_new[cur.next]
            new_node.random = old_to_new[cur.random]

            cur = cur.next
            
        #map the original linked lists' head to copy.
        return old_to_new[head]
        
        
        
        
        