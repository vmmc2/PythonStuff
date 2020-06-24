# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
answer = True

def checkBST(root: TreeNode, MIN_VALUE: int, MAX_VALUE: int) -> None:
    global answer
    if root == None:
        return
    if root.val <= MIN_VALUE or root.val >= MAX_VALUE:
        answer = False
        return
    checkBST(root.left, MIN_VALUE, root.val)
    if answer == False: # Already discovered that the binary tree is not a BST.
        return
    checkBST(root.right, root.val, MAX_VALUE)
    if answer == False: # Already discovered that the binary tree is not a BST.
        return
    return

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Treating the corner cases...
        global answer
        answer = True
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        MAX_VALUE = 2**32
        MIN_VALUE = 2**32 * (-1)
        checkBST(root, MIN_VALUE, MAX_VALUE)
        return answer
        
        
