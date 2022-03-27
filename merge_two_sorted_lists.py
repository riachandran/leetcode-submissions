# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        n = list1
        while n is not None:
            l1_list.append(n.val)
            n = n.next
        l2_list = []
        m = list2
        while m is not None:
            l2_list.append(m.val)
            m = m.next
        final_list = l1_list + l2_list
        output = sorted(final_list)
        if(output == []):
            return list1
        else:
            head = ListNode(output[0])
            tail = head
            e = 1
            while e < len(output):
                tail.next = ListNode(output[e])
                tail = tail.next
                e+=1
            return head
