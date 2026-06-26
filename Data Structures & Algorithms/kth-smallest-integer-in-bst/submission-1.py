# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def dfs(node):
            if not node:
                return
            if len(stack) >= k:
                return 
            left = dfs(node.left)
            stack.append(node.val)
            right = dfs(node.right)
            
            return

        dfs(root)
        return stack[k-1]








        # stack = []
        # curr = root

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return curr.val
        #     curr = curr.right



        