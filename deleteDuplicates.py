# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res
        seen = set()
        
        while head:
            if head.val not in seen:
                seen.add(head.val)
                dummy.next = ListNode(head.val)
                dummy = dummy.next
            head = head.next
            
        return res.next
