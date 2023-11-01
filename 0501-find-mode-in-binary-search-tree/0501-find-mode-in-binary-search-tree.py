# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        curr_streak = 0
        max_streak = 0
        curr_num = 0
        ans = []

        def dfs(node):
            if not node:
                return 
            
            nonlocal curr_streak
            nonlocal max_streak
            nonlocal curr_num
            nonlocal ans

            dfs(node.left)
            if node.val != curr_num:
                curr_num = node.val
                curr_streak = 0

            curr_streak += 1

            if curr_streak == max_streak:
                ans.append(curr_num)
            
            if curr_streak > max_streak:
                ans = []
                ans.append(curr_num)
                max_streak = curr_streak

            dfs(node.right)

        dfs(root)
        return ans