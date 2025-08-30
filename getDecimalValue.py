# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decL = list()

        while head:
            decL.append(str(head.val))
            head = head.next


        return int("".join(decL),2)
