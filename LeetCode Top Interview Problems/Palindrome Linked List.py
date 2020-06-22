# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head: ListNode) -> ListNode:
    # Treating the corner cases
    if head == None:
        return head
    if head.next == None:
        return head
    # Treating the general cases:
    curr = head
    prev = None
    nxt = head.next
    while curr.next != None:
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next
    curr.next = prev
    return curr
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Treating the corner cases first:
        if head == None:
            return True
        if head.next == None:
            return True
        #Treating the general cases:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        fast = head
        slow = reverseList(slow)
        while slow != None:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
