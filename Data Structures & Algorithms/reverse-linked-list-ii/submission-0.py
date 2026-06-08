# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        left_prev, curr = dummy, head

        for _ in range(left-1):
            left_prev, curr = curr, curr.next
        
        prev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next =  prev
            prev = curr
            curr = tmp
        
        left_prev.next.next = curr
        left_prev.next =prev

        return dummy.next

               
