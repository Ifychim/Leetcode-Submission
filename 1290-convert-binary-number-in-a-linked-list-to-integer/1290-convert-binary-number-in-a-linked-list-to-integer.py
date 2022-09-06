# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #O(n) solution.
        temp = head
        result = ""
        
        while temp != None:
            
            result += str(temp.val)
            temp = temp.next
        
        #base 2 for a binary number.
        result = int(result,2)
        
        return result
