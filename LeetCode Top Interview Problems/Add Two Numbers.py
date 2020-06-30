# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0, None) # Criando uma lista com node sentinela
        curr = result
        carry = 0
        currA = l1
        currB = l2
        while currA != None and currB != None:
            soma = currA.val + currB.val + carry
            if soma <= 9:
                curr.next = ListNode(soma, None)
                curr = curr.next
                carry = 0
            else:
                soma = soma % 10
                curr.next = ListNode(soma, None)
                curr = curr.next
                carry = 1
            currA = currA.next
            currB = currB.next
        while currA != None:
            soma = currA.val + carry
            if soma <= 9:
                curr.next = ListNode(soma, None)
                curr = curr.next
                carry = 0
            else:
                soma = soma % 10
                curr.next = ListNode(soma, None)
                curr = curr.next
                carry = 1
            currA = currA.next
        while currB != None:
            soma = currB.val + carry
            if soma <= 9:
                curr.next = ListNode(soma, None)
                curr = curr.next
                carry = 0
            else:
                soma = soma % 10
                curr.next = ListNode(soma, None)
                curr = curr.next
                carry = 1
            currB = currB.next
        if carry == 1:
            curr.next = ListNode(1, None)
            curr = curr.next
        return result.next
        
