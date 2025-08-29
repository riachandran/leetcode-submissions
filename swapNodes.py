# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        count = 0

        if head.next == None:
            return head

        while curr:
            count += 1
            curr = curr.next

        first_half = head
        second_half = head

        for _ in range(k - 1):
            first_half = first_half.next

        for _ in range(count - k):
            second_half = second_half.next

        first_half.val,second_half.val = second_half.val,first_half.val

        return head
