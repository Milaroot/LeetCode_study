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
    vector<int> arr;
    void dfs(TreeNode* root){
        if(!root) return;
        arr.push_back(root->val);
        dfs(root->left);
        dfs(root->right);
    }
    
    void iot(TreeNode* root){
        if(!root) return;
        iot(root->left);
        int size = arr.size() - 1;
        root->val = arr[size];
        arr.pop_back();
        iot(root->right);
    }
    
    void recoverTree(TreeNode* root) {
        dfs(root);
        sort(arr.begin(), arr.end());
        reverse(arr.begin(), arr.end());
        iot(root);
    }
};