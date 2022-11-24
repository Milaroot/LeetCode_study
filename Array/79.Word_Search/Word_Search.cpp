class Solution {
public:
    bool flag = false;
    
    void DFS(vector<vector<char>>& board, string word, int ptr, int i, int j){
        if(flag == true) return;
        
        if(ptr == word.size()){
            flag = true;
            return;
        }
        
        board[i][j] = '%';
        
        if(i > 0 && board[i - 1][j] == word[ptr]){ 
            DFS(board, word, ptr + 1, i - 1, j);
        }
        
        if(j > 0 && board[i][j - 1] == word[ptr]){ 
            DFS(board, word, ptr + 1, i, j - 1);
        }
        
        
        if(i < board.size() - 1 && board[i + 1][j] == word[ptr]){ 
            DFS(board, word, ptr + 1, i + 1, j);
        }
        if(j < board[i].size() - 1 && board[i][j + 1] == word[ptr]){ 
            DFS(board, word, ptr + 1, i, j + 1);
        }
        
        board[i][j] = word[ptr - 1];
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i = 0; i < board.size(); ++i){
            for(int j = 0; j < board[i].size(); ++j){
                if(board[i][j] == word[0]) {
                    DFS(board, word, 1, i, j);
                }
                if(flag == true) break;
            }
        }
        return flag;
    }
};