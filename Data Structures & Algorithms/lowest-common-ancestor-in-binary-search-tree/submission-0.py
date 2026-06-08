# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        if not root:
            return None

        if root.val > high:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < low:
            return self.lowestCommonAncestor(root.right, p, q)

        # low <= root.val <= high
        return root

            
