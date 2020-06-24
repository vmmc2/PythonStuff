# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
answer = 0
stack = []

def traversal(root: TreeNode) -> None:
    if root == None:
        return
    global stack
    stack.append(root.val)
    global answer
    answer = max(answer, len(stack))
    traversal(root.left)
    traversal(root.right)
    stack.pop()
    return
    
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        global answer
        answer = 0
        global stack
        stack = []
        # Treating the corner cases first
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            traversal(root)
            return answer
        
