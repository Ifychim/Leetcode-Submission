# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []

        curr = head
        
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        
        low = 0
        high = len(arr)-1

        while low <= high:
            if arr[low] != arr[high]:
                return False
            low += 1
            high -= 1
            
        return True