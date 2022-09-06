# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        temp = head
        result = ""
        
        while temp != None:
            
            result += str(temp.val)
            temp = temp.next
        
        result = int(result,2)
        
        return result