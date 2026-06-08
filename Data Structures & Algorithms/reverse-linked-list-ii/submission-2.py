# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        prev, curr = dummy, head

        idx = 1

        while idx < left:
            prev, curr = curr, curr.next
            idx += 1
        # curr: l, prev: point to curr/l, idx: l

        prev2 = None
        while idx <= right:
            tmp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = tmp
            idx += 1
        # curr: r+1, prev2 = r, curr.next: poinr to after r, idx r+1`
        prev.next.next = curr
        prev.next = prev2

        return dummy.next
        





        # dummy = ListNode()
        # dummy.next = head
        
        # left_prev, curr = dummy, head

        # for _ in range(left-1):
        #     left_prev, curr = curr, curr.next
        
        # prev = None
        # for _ in range(right - left + 1):
        #     tmp = curr.next
        #     curr.next =  prev
        #     prev = curr
        #     curr = tmp
        
        # left_prev.next.next = curr
        # left_prev.next =prev

        # return dummy.next

               
