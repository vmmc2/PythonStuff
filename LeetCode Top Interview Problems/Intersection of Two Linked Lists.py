# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Treating the corner cases...
        if headA == None:
            return headA
        if headB == None:
            return headB
        currA = headA
        currB = headB
        while currA != currB:
            currA = currA.next
            currB = currB.next
            if currA == None and currB == None:
                break
            if currA == None:
                currA = headB
            if currB == None:
                currB = headA
        return currA
