# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #DFS will calculate the height only (max of left and right)
        def dfs(root):
            #base case
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            dia = left+right
            self.res = max(self.res, dia)
            return 1+max(left, right)
        dfs(root)
        return self.res
            



        