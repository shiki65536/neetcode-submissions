# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)

            l_balance, l_len = dfs(node.left)
            r_balance, r_len = dfs(node.right)
            c_len = max(l_len, r_len) + 1
            
            if not r_balance or not l_balance:
                return (False,  c_len)
            elif abs(l_len - r_len) > 1:
                return (False, c_len)
            
            return (True, c_len)

        return dfs(root)[0]














        # def dfs(node):
        #     if not node:
        #         return (0, True)
        #     left, left_result = dfs(node.left)
        #     right, right_result = dfs(node.right)
        #     height = max(left, right) + 1

        #     if abs(left - right) > 1 or not left_result  or not right_result:
        #         return (height, False) 
        #     else:
        #         return (height, True)
        
        # _, result = dfs(root)
        # return result 
















        # if not root:
        #     return True
        # def getHeight(node):
        #     if not node:
        #         return 0
        #     left, right = getHeight(node.left), getHeight(node.right)
        #     if right == -1 or left == -1:
        #         return -1
        #     if abs(left - right) > 1:
        #         return -1
        #     return 1 + max(left, right)
        

        # return False if getHeight(root) == -1 else True