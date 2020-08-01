# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, preStart: int, inStart: int, inEnd: int, preorder: List[int], inorder: List[int]) -> TreeNode:
        if (preStart > len(preorder) - 1) or inStart > inEnd :
            return None
        
        root = TreeNode(preorder[preStart])
        inIndex = 0
        for i in range(inStart, inEnd + 1):
            if inorder[i] == root.val:
                inIndex = i
                break
        root.left = self.helper(preStart + 1, inStart, inIndex - 1, preorder, inorder)
        root.right = self.helper(preStart + 1 + (inIndex - inStart) , inIndex + 1, inEnd, preorder, inorder)
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder)
