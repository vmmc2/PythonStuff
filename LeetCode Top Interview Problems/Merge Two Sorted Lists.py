# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0, None) # node sentinela
        curr1 = l1
        curr2 = l2
        temp = head
        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                temp.next = ListNode(curr1.val, None)
                temp = temp.next
                curr1 = curr1.next
            else:
                temp.next = ListNode(curr2.val, None)
                temp = temp.next
                curr2 = curr2.next
        while curr1 != None:
            temp.next = ListNode(curr1.val, None)
            temp = temp.next
            curr1 = curr1.next
        while curr2 != None:
            temp.next = ListNode(curr2.val, None)
            temp = temp.next
            curr2 = curr2.next
        return head.next
