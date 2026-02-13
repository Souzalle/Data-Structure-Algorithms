"""
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.

A leaf is a node with no children.

"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # Se não houver root, nao há arvore. Retorna falso
            return False
        
        if not root.right and not root.left and targetSum - root.val == 0:
            return  True # se n ha right nem left ent é uma folha. Se ele chegar em uma folha cujo valor dela menos o target atual der 0 ent temos um caminho
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        # ele passa para a esquerda e para direita sempre subtraindo o valor do nó atual do target