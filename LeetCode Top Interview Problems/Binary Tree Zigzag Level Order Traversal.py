# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # Percebi que tem um jeito bem mais facil de resolver esse problema
        answer = []
        # Treating corner case
        if root == None: # empty tree
            return answer
        #Treating the general cases...
        fila = deque()
        fila.append(root)
        while len(fila) > 0:
            tam = len(fila)
            pseudo = []
            for i in range(0, tam):
                x = fila.popleft()
                pseudo.append(x.val)
                if x.left != None:
                    fila.append(x.left)
                if x.right != None:
                    fila.append(x.right)
            answer.append(pseudo)
        for i in range(0, len(answer)):
            if i % 2 != 0:
                answer[i].reverse()
        return answer
