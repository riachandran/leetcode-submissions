# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_list = []
        n = l1
        while n is not None:
            l1_list.append(n.val)
            n = n.next
        l2_list = []
        m = l2
        while m is not None:
            l2_list.append(m.val)
            m = m.next
        l1_list.reverse()
        l2_list.reverse()

        num1 = int("".join([str(i) for i in l1_list]))
        num2 = int("".join([str(i) for i in l2_list]))
        sum = str(num1 + num2)
        sum_rev = sum[::-1]
        output = [int(a) for a in sum_rev]
        head = ListNode(output[0])
        tail = head
        e = 1
        while e < len(output):
            tail.next = ListNode(output[e])
            tail = tail.next
            e+=1
        return head
