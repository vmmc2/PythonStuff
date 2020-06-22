# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        tam = 0
        while curr != None: # Contando quantos nodes existem na linked list.
            tam += 1
            curr = curr.next
        answer = tam - n
        curr = head
        tam = 1
        if answer == 0: # tem que retirar logo de cara o primeiro elemento.
            return head.next
        # nesse caso, eu posso retirar qualquer outro elemento da linked list.
        while tam != answer:
            tam += 1
            curr = curr.next
        curr.next = curr.next.next
        return head
        
