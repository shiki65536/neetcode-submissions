# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue = deque([(p,q)])
        while queue:
            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            elif n1.val != n2.val:
                return False
            else:
                left = (n1.left, n2.left)
                right = (n1.right, n2.right)
                queue.append(left)
                queue.append(right)
        
        return True

