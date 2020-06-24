# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def buildBST(root: TreeNode, nums: List[int], left: int, right: int) -> TreeNode:
    if left > right:
        return None
    mid = (left + right)//2
    root = TreeNode(nums[mid])
    root.left = buildBST(root.left, nums, left, mid - 1) 
    root.right = buildBST(root.right, nums, mid + 1, right)
    return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = None
        # Corner case that I received an empty list, so I must return an empty tree
        if len(nums) == 0:
            return root
        # Now, I just apply binary search to construct the BST
        left = 0
        right = len(nums) - 1
        return buildBST(root, nums, left, right)
        
        
