# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if not head:
            return None
        while cur:
            if cur.next == None:
                break
            elif cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
            