/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class BSTIterator {
public:
    int ptr = 0;
    vector<int> Nodes = {-1};
    
    BSTIterator(TreeNode* root) {
        INORDER_DFS(root);
    }
    
    void INORDER_DFS(TreeNode* root){
        if(!root) return;
        INORDER_DFS(root->left);
        Nodes.push_back(root->val);
        INORDER_DFS(root->right);
    }

    int next() {
        ptr++;
        return Nodes[ptr];
    }
    
    bool hasNext() {
        return ptr+1 < Nodes.size();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */