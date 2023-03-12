# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Time : O(n log n), Space : O(log n)
    def constructBST(self, left: ListNode, right: ListNode) -> TreeNode:
        if left == right:
            return None
        slow, fast = left, left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.constructBST(left, slow)
        root.right = self.constructBST(slow.next, right)
        return root


    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        return self.constructBST(head, None)