# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        res = ListNode(0)
        dummy = res
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        while slow:
            dummy.next = ListNode(slow.val)
            dummy = dummy.next
            slow = slow.next
            
        return res.next
