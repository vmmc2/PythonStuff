# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Tentar resolver com dicionarios/map
        d = {}
        curr = head
        while curr != None:
            if curr in d:
                return True # Achei um ciclo na minha lista
            else:
                d[curr] = 1
            curr = curr.next
        return False
