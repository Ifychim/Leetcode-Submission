# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        #Replace the node to be deleted with the next node in the LL
        #Delete next node in the LL
        nextNode = node.next
        
        node.val = nextNode.val
        node.next = nextNode.next
        
        nextNode.next = None
        del(nextNode)
        