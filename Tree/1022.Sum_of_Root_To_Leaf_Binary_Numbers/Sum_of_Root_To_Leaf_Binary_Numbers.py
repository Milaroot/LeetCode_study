# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_num(self, bn: str) -> int:
        return int(bn, 2)   
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        treeleaf = []
        curr = ""
        self.ans = 0
        def dfs(root, curr):
            if not(root.left) and not(root.right):
                self.ans += self.get_num(curr + str(root.val))
                return 0
            if root.left: dfs(root.left, curr + str(root.val))
            if root.right:dfs(root.right, curr + str(root.val))
            return 0
              
        dfs(root, curr)
        return self.ans
            
            