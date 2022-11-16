"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        stack = []
        
        while curr:
              
            #if current node is pointing to a none-null child, we need to flatten it
            if curr.child != None:
                #if there is a subsequent link, store it to be appended to linked list at a later point
                if curr.next:
                    stack.append(curr.next)
                
                #3 pointers need to be updated: next, childs' prev, child of curr
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            
        #once we hit tail node, we need to see if there are some links to be appended to the first level
            if curr.next == None and len(stack) > 0:
                curr.next = stack.pop()
                curr.next.prev = curr
                
            curr = curr.next
            
        return head
        