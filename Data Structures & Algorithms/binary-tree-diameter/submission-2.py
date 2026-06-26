# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        MAX_LEN = 0
        def dfs(node):
            nonlocal MAX_LEN
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            MAX_LEN = max(MAX_LEN, left, right, left + right)

            return max(left, right) + 1
        
        dfs(root)
        
        return MAX_LEN