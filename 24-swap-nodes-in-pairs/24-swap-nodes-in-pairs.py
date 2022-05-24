# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        cur = head
        while cur and cur.next:
            #storing values
            second = cur.next
            nxtPair = cur.next.next
            
            #swap
            second.next = cur
            cur.next = nxtPair
            prev.next = second
            
            #update
            prev = cur
            cur = nxtPair
            
        return dummy.next
            
            