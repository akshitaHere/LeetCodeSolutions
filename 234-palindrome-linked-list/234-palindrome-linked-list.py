# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #finding middle element
        t, h = head, head
        while h and h.next:
            h = h.next.next
            t = t.next
        
        #reversing second half of ll
        prev = None
        while t:
            temp = t.next
            t.next = prev
            prev = t
            t = temp
        
        #checking
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True