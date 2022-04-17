# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def dfs(root):
            if root == None: return
            dfs(root.right)
            ans.append(root.val)
            dfs(root.left)
        dfs(root)
        
        head = TreeNode(ans.pop())
        last = head
        while(len(ans) != 0):
            newnode = TreeNode(ans.pop())
            last.right = newnode
            last = last.right
        return head
        
        
        