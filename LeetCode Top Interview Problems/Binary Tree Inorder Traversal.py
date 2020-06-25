# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
answer = []

def traversal(root: TreeNode) -> None:
    if root == None:
        return
    traversal(root.left)
    global answer
    answer.append(root.val)
    traversal(root.right)
    return

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        global answer
        answer = []
        traversal(root)
        return answer
