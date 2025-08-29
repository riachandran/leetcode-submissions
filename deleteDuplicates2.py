# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        curr = dummy.next
         
        while curr:
            remove = False
            while curr.next and curr.val == curr.next.val:
                prev.next = curr.next = curr.next.next
                remove = True

            if not remove:
                prev = curr

            curr = curr.next

        return dummy.next
