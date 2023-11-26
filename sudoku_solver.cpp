class Solution {

public:
    bool isValid(vector<vector<char>>& board, int row, int col, char ch) {
        const int subgrid_size = 3;
        const int board_size = 9;
        int sub_grid_row = row / 3, sub_grid_col = col / 3;

        for (int k = 0; k < subgrid_size; k++) {
            for (int l = 0; l < subgrid_size; l++) {
                if (board[sub_grid_row * subgrid_size + k][sub_grid_col * subgrid_size + l] == ch) 
                    return false;
            }
        }

        for (int k = 0; k < board_size; k ++){
            if (board[k][col] == ch) 
                return false;
            if (board[row][k] == ch) 
                return false;
        }

        return true;
    }

public:
    bool solve(vector<vector<char>>& board) {
        const int subgrid_size = 3;
        const int board_size = 9;
        bool break_flag = false;
        set<int> candidates;

        for (int i = 0; i < board_size; i++) {
            if (break_flag) break;
            for (int j = 0; j < board_size; j++) {
                if (board[i][j] == '.') {
                    for (int c = 1; c <= board_size; c++) {
                        if (isValid(board, i, j, c + '0')) {
                            board[i][j] = c + '0';
                            if (solve(board)) return true;
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }

};