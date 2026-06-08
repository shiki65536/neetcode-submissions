# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            if key < node.val:
                node.left = dfs(node.left)
            elif key > node.val:
                node.right = dfs(node.right)
            else:
                # found node to delete
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # both children exist: use successor
                successor = node.right
                while successor.left:
                    successor = successor.left

                node.val = successor.val
                node.right = delete_min(node.right)

            return node

        def delete_min(node):
            if not node.left:
                return node.right
            node.left = delete_min(node.left)
            return node

        return dfs(root)

            
            