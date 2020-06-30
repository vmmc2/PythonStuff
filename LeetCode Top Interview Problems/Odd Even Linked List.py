# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ## Treating the corner cases first...
        if head == None:
            return head
        if head.next == None:
            return head
        ## Treating the general cases...
        currOdd = head
        headEven = head.next
        currEven = head.next
        while currOdd != None and currEven != None and currEven.next != None and currOdd.next != None:
            currOdd.next = currEven.next
            currOdd = currOdd.next
            currEven.next = currOdd.next
            currEven = currEven.next
        currOdd.next = headEven
        return head
        
