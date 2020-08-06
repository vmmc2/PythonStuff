# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Solving the problem for the corner cases first:
        if head == None:   # Empty list.
            return head
        if head.next == None:   # List with only one node.
            return head
        # Solving the problem for the general case:
        currOdd = head
        evenHead = head.next
        currEven = head.next
        while currOdd != None and currEven != None and currOdd.next != None and currEven.next != None:
            currOdd.next = currEven.next
            currOdd = currEven.next
            currEven.next = currOdd.next
            currEven = currOdd.next
        currOdd.next = evenHead
        return head
            
        
