# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 1
        dummy = ListNode(next = head)
        prev = dummy
        slow, fast = head, head
        
        while cnt < n+1:
            cnt += 1
            fast = fast.next
        #print(fast)
        while fast:
            fast = fast.next
            slow = slow.next
            prev = prev.next
        #print(prev,'\n',slow,'\n',fast)
        prev.next = slow.next
        slow = slow.next
        return dummy.next