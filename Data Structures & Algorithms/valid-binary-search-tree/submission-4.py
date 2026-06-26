# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, maxval, minval):
            if not node:
                return True
            if not minval < node.val < maxval:
                return False
            left = dfs(node.left, node.val, minval)
            right = dfs(node.right, maxval, node.val)

            if not left or not right:
                return False
            
            return True
        
        return dfs(root, math.inf, -math.inf)






        # if not root:
        #     return True
        # def isValid(node: Optional[TreeNode], maxVal, minVal) -> bool:
        #     if not node:
        #         return True
        #     if not minVal < node.val < maxVal:
        #         return False
        #     return (
        #         isValid(node.left, node.val, minVal) 
        #         and
        #         isValid(node.right, maxVal, node.val)
        #     )
        
        # return isValid(root, math.inf, -math.inf)
        # if not root:
        #     return True

        # queue = deque([(root, float("-inf"), float("inf"))])
        # while queue:
        #     node, low, high = queue.popleft()
        #     if not low < node.val < high:
        #         return False
        #     if node.left:
        #         queue.append((node.left, low, node.val))
        #     if node.right:
        #         queue.append((node.right, node.val, high))
        
        # return True