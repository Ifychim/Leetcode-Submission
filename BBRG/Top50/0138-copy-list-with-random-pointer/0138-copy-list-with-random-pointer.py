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
        old_to_new = {None:None} #initialize the dictionary with none values for the edge case where a random pointer points to none
        
        curr = head
        
        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            
            curr = curr.next
            
        curr = head
        
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next]
            new_node.random = old_to_new[curr.random]
            
            curr = curr.next
            
        return old_to_new[head]