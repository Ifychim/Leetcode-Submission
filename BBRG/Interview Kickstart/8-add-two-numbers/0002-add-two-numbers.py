# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_nums = deque()
        l2_nums = deque()
        
        curr1, curr2 = l1, l2
        
        while curr1 != None:
            l1_nums.appendleft(curr1.val)
            curr1 = curr1.next
        
        while curr2 != None:
            l2_nums.appendleft(curr2.val)
            curr2 = curr2.next
        
        l1_num, l2_num = '',''
        
        for num in l1_nums:
            l1_num += str(num)
            
        for num in l2_nums:
            l2_num += str(num)
            
        addition = int(l1_num) + int(l2_num)
        addition_arr = deque()
        
        for num in str(addition):
            addition_arr.appendleft(num)
        
        return ListNode(val=','.join(addition_arr))