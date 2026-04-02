# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root,res):
            if not root:
                return None
            inOrder(root.left,res)
            res.append(root.val)
            inOrder(root.right,res)

        result_list = []
        inOrder(root, result_list)
        print(result_list)
        return result_list[k-1]