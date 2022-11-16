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
        
        stack = [] #stack holds sub-list of nodes which have children pointers pointing to another node
        curr = head
        
        while curr:
            #if our current node has a child, pointing to another level do 2 things:
            #1 - store sub list in stack
            #2 - update pointers of curr. (next = child, child.prev = curr, child = none)
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
                
#if we reach the end of our list, we want to append sub-lists which were removed from earlier.
#and update pointers
            if curr.next == None and len(stack) > 0:
                curr.next = stack.pop()
                curr.next.prev = curr
                
            curr = curr.next
            
        return head