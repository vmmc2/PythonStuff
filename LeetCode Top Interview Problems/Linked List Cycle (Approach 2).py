# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # First of all, treating the corner cases:
        if head == None:
            return False
        if head.next == None:
            return False
        slow = head
        fast = head
        while slow.next != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True # Found a cycle.
        return False # There is no cycle in the linked list.
