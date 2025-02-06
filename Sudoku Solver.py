class Solution {
 public:
  void solveSudoku(vector<vector<char>>& board) {
    solve(board, 0);
  }

 private:
  // Backtracking function to fill the Sudoku board
  bool solve(vector<vector<char>>& board, int s) {
    if (s == 81)  // If we've filled all 81 cells, the board is solved
      return true;

    const int i = s / 9;  // Get row index
    const int j = s % 9;  // Get column index

    if (board[i][j] != '.')  // Skip already filled cells
      return solve(board, s + 1);

    for (char c = '1'; c <= '9'; ++c) {
      if (isValid(board, i, j, c)) { // Check if placing 'c' is valid
        board[i][j] = c;  // Place the number
        if (solve(board, s + 1))  // Recur to solve the next cell
          return true;
        board[i][j] = '.';  // Backtrack if no solution is found
      }
    }

    return false;  // No valid number found for this cell
  }

  // Function to check if placing 'c' at (row, col) is valid
  bool isValid(vector<vector<char>>& board, int row, int col, char c) {
    for (int i = 0; i < 9; ++i)
      if (board[i][col] == c || board[row][i] == c ||  // Check row & column
          board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) // Check 3x3 box
        return false;
    return true;
  }
};
