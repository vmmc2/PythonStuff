# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque # deque eh mais recomendado para ser usado como uma fila do que se a gente usar uma list.

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = []
        # Treating corner case
        if root == None: # Received an empty tree as input
            return answer
        fila = deque()
        fila.append(root)
        while len(fila) > 0:
            tam = len(fila)
            p = []
            for i in range(0, tam):
                x = fila.popleft()
                p.append(x.val)
                if x.left != None:
                    fila.append(x.left)
                if x.right != None:
                    fila.append(x.right)
            answer.append(p)
        return answer
