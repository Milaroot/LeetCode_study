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
class Solution {
public:
    int mx = 0;
    void dfs(TreeNode *root, int curr){
        if(root != nullptr){
            curr += 1;
            mx = max(mx, curr);
            dfs(root->left, curr);
            dfs(root->right, curr);
        }
    }
    int maxDepth(TreeNode* root) {
        int curr = 0;
        dfs(root, curr);
        return mx;
    }
};
