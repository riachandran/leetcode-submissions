# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        totalcount = 0
        curr = head

        while curr:
            totalcount += 1
            curr = curr.next

        if (totalcount == n): return head.next

        curr = head

        while curr:
            if count == totalcount - n:
                curr.next = curr.next.next

            count += 1
            curr = curr.next

        return head
