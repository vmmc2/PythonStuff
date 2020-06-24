# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def checkSym(left: TreeNode, right: TreeNode) -> bool:
    if left == None and right == None:
        return True
    if left == None and right != None:
        return False
    if left != None and right == None:
        return False
    if left.val != right.val:
        return False
    return checkSym(left.left, right.right) and checkSym(left.right, right.left)
    

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Treating the corner cases...
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        return checkSym(root.left, root.right)
