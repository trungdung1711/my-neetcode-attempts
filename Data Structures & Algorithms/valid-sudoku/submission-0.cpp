class Solution {
public:
    struct pair_hash {
        size_t operator()(const std::pair<int,int>& p) const {
            return std::hash<int>()(p.first) ^ (std::hash<int>()(p.second) << 1);
        }
    };

    bool isValidSudoku(vector<vector<char>>& board) {
        // row (0, 99) -> (8, 99)       = 9
        // column (99, 0) -> (99, 8)    = 9
        // box (0, 0) -> (2, 2)         = 9

        // index (0, 0) -> (8, 8)
        // first -> row -> check (row, 99)
        // second -> column -> check (99, column)
        // (first, second) -> check (first / 3, second / 3)

        std::unordered_map<
            std::pair<int,int>,
            std::unordered_map<int,bool>,
            pair_hash
        > m;

        for (std:: size_t i = 0; i < 9; ++i) {
            for (std:: size_t j = 0; j < 9; ++j) {
                // checking for filled cells
                if (board[i][j] == '.') continue;

                // row
                std:: unordered_map<int, bool>& rowCheck = m[std:: pair(i, 99)];
                if (rowCheck.find(board[i][j]) != rowCheck.end()) {
                    // found
                    return false;
                } else {
                    // not found
                    rowCheck[board[i][j]] = true;
                }

                // column
                std:: unordered_map<int, bool>& columnCheck = m[std:: pair(99, j)];
                if (columnCheck.find(board[i][j]) != columnCheck.end()) {
                    // found
                    return false;
                } else {
                    // not found
                    columnCheck[board[i][j]] = true;
                }

                // box
                std:: unordered_map<int, bool>& boxCheck = m[std:: pair(i / 3, j / 3)];
                if (boxCheck.find(board[i][j]) != boxCheck.end()) {
                    // found
                    return false;
                } else {
                    // not found
                    boxCheck[board[i][j]] = true;
                }
            }
        }

        return true;
    }
};