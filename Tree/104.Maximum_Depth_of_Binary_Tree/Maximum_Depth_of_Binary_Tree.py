# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mx = 0
        
    def dfs(self, root, curr):
        if root:
            curr += 1
            self.mx = max(self.mx, curr)
            self.dfs(root.left, curr)
            self.dfs(root.right, curr)
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = 0
        self.dfs(root, curr)
        return self.mx