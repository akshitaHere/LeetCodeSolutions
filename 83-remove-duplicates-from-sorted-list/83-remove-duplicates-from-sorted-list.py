# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        first = head
        while first != None:
            if first.next == None:
                break
            elif first.val == first.next.val:
                first.next = first.next.next
            else:
                first = first.next
        
        
        return head
        
        
        