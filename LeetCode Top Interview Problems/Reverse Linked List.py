# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Tratando os casos base antes de lidar com o caso geral
        if head == None:
            return head
        if head.next == None:
            return head
        prev = None
        curr = head
        nxt = curr.next
        while True:
            curr.next = prev
            if nxt == None:
                break
            prev = curr
            curr = nxt
            nxt = nxt.next
        return curr
            
