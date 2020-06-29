# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
li = []

def traversal(root: TreeNode, kth: int) -> None:
    if root == None:
        return
    global li
    traversal(root.left, kth)
    if len(li) == kth:
        return
    li.append(root.val)
    traversal(root.right, kth)
    if len(li) == kth:
        return
    return

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        global li
        li = []
        traversal(root, k)
        return li[-1]
