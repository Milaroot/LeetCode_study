# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.ptr = 0
        self.Nodes = [-1]
        self.DFS(root)
        self.Nodes_length = len(self.Nodes)
    def DFS(self, root):
        if(root == None): return 
        self.DFS(root.left)
        self.Nodes.append(root.val)
        self.DFS(root.right)
    def next(self) -> int:
        self.ptr += 1
        return self.Nodes[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr + 1 < self.Nodes_length 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()