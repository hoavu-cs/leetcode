#include <iostream>
#include <vector>
#include <set>
#include <tuple>

using namespace std;

void printNestedVector(const std::vector<std::vector<std::set<char>>>& nestedVector) {
    for (const auto& outerVec : nestedVector) {
        for (const auto& innerSet : outerVec) {
            std::cout << "{";
            for (char ch : innerSet) {
                std::cout << ch << " ";
            }
            std::cout << "} ";
        }
        std::cout << std::endl;
    }
}

void printBoard(const vector<vector<char>>& board) {
    for (const auto& outerVec : board) {
        for (const auto& innerSet : outerVec) {
            std::cout << innerSet << " ";
        }
        std::cout << std::endl;
    }
}

class Solution {

public:

    void solve(vector<vector<char>>& board, set<tuple<int, int>>& empty_cells){
        const int subgrid_size = 3;
        const int board_size = 9;
        bool break_flag = false;
        set<int> candidates;

        for (int c = 1; c <= board_size; c++)
            candidates.insert(c);

        if (empty_cells.empty()) return;
        
        // get the next empty cell
        tuple <int, int> next_cell = *empty_cells.begin(); 
        empty_cells.erase(empty_cells.begin());

        int i = get<0>(next_cell), j = get<1>(next_cell);
        int sub_grid_row = i / 3, sub_grid_col = j / 3;

        for (int k = 0; k < subgrid_size; k++) {
            for (int l = 0; l < subgrid_size; l++) {
                int element = board[sub_grid_row * subgrid_size + k][sub_grid_col * subgrid_size + l];
                if (element != '.') 
                    candidates.erase(element - '0');
            }
        }

        for (int k = 0; k < board_size; k ++){
            if (board[k][j] != '.') 
                candidates.erase(board[k][j] - '0');
            if (board[i][k] != '.') 
                candidates.erase(board[i][k] - '0');
        }

        // if there is no candidate, return. Set the top left element to '0' to indicate failure.
        if (candidates.empty()) {
            board[0][0] = '0';
            empty_cells.insert(empty_cells.begin(), next_cell);
            return;
        } 
        // try each possible candidate
        for(int c : candidates) {
            char top_left = board[0][0];
            board[i][j] = c + '0';
            solveSudoku(board);
            if (board[0][0] != '0') return;
            board[0][0] = top_left;
            board[i][j] = '.';
        }
        // if no candidate works, return. Set the top left element to '0' to indicate failure.
        board[0][0] = '0';
        empty_cells.insert(empty_cells.begin(), next_cell);
    }

    void solveSudoku(vector<vector<char>>& board) {
        set<tuple<int, int>> empty_cells;
        const int board_size = 9;
        const int subgrid_size = 3;
        for (int i = 0; i < board_size; i++) 
            for (int j = 0; j < board_size; j++) 
                if (board[i][j] == '.') 
                    empty_cells.insert(make_tuple(i, j));
        solve(board, empty_cells);
    }
};



int main() {
    Solution s;
    vector<vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}};
    s.solveSudoku(board);
    printBoard(board);
    return 0;
}