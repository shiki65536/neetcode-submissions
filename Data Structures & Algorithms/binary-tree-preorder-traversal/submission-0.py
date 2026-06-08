# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(node):
            if not node:
                return
            output.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return output



        # output = []
        # queue = deque([root])

        # while queue:
        #     cur = queue.popleft()
        #     output.append(cur.val)
        #     if cur.left:
        #         queue.append(cur.left)
        #     if cur.right:
        #         queue.append(cur.right)
        
        # return output

        


        