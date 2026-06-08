# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def getHeight(node):
            if not node:
                return 0
            left, right = getHeight(node.left), getHeight(node.right)
            if right == -1 or left == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        

        return False if getHeight(root) == -1 else True