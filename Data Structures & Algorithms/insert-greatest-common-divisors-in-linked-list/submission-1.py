from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def dfs(node, nxt):
            if nxt:
                val = gcd(node.val, nxt.val)
                new = ListNode(val, nxt)
                node.next = new
                dfs(nxt, nxt.next)
            return node

        return dfs(head, head.next)