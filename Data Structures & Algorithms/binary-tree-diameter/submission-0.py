# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Brute Force
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Always include the base case
        if not root:
            return 0
        leftheight = self.maxHeight(root.left)
        rightheight = self.maxHeight(root.right)
        leftheight = self.maxHeight(root.left)
        diameter   = leftheight + rightheight
        return max(
            diameter,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
            )
    def maxHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
        





        