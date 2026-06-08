# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSame(p, q):
            queue = deque([(p, q)])
            while queue:
                n1, n2 = queue.popleft()
                if not n1 and not n2:
                    continue
                if not n1 or not n2:
                    return False
                if n1.val != n2.val:
                    return False
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
            return True

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and isSame(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False


        
