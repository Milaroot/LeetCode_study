# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = defaultdict(int)
        self.flag = 0
        
    def dfs(self, root, k):
            
            if not(root): return
            if self.flag == 1: return
            if self.dic[root.val] == 1: 
                self.flag = 1
                return 
            
            self.dic[k - root.val] = 1
            
            
            
            self.dfs(root.left, k)
            self.dfs(root.right, k)
            
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        self.dfs( root, k)
        
        return self.flag == 1
            
            
            