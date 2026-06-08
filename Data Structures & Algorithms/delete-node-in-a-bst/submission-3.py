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
            elif node.val < key:
                node.right = dfs(node.right)
            elif node.val > key:
                node.left = dfs(node.left)
            else: # node.val == key
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
    
                successor = node.left
                while successor.right:
                    successor = successor.right

                node.val = successor.val
                node.left = delete_min(node.left)

            return node
        
        def delete_min(node):
            if not node.right:
                return node.left
            node.right = delete_min(node.right)
            return node

        return dfs(root)

            
            