# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(Node, left, right):
            if not Node:
                return True
            if not (left < Node.val < right):
                return False
            return valid(Node.left,left,Node.val) and valid(Node.right,Node.val,right)
        return valid(root,float('-inf'),float('inf'))