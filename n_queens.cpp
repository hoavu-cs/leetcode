#include <algorithm>

class Solution {
private:
    vector<vector<string>> solutions;

public:

    bool is_valid(const vector<string>& board, int row, int col) {
        int n = board.size();

        // Check the column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }

        // Check the upper left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        // Check the upper right diagonal
        for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    void solve(vector<string>& board, int row) {
        int n = board.size();
        
        for(int col = 0; col < n; col++) {
            if (is_valid(board, row, col)) {
                board[row][col] = 'Q';
                if (row < n - 1) { 
                    solve(board, row + 1);
                } else {
                    vector<string> next_valid_board = board;
                    solutions.push_back(next_valid_board);
                }
                board[row][col] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<string> board  (n, string(n, '.'));
        solve(board, 0);
        return solutions;
    }
};
