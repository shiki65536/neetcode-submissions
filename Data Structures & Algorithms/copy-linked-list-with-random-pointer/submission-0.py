"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_list = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copy_list[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            node = copy_list[curr]
            node.next = copy_list[curr.next]
            node.random = copy_list[curr.random]
            curr = curr.next
        
        return copy_list[head]