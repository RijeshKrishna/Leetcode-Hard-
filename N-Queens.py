class Solution {
 public:
  vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> ans;
    // Start DFS with an empty board and availability flags for columns and diagonals
    dfs(n, 0, vector<bool>(n), vector<bool>(2 * n - 1), vector<bool>(2 * n - 1),
        vector<string>(n, string(n, '.')), ans);
    return ans;
  }

 private:
  void dfs(int n, int i, vector<bool>& cols, vector<bool>& diag1,
           vector<bool>& diag2, vector<string>& board,
           vector<vector<string>>& ans) {
    if (i == n) {
      // If we've placed queens in all rows, add the current board to the result
      ans.push_back(board);
      return;
    }

    // Try placing a queen in each column of row i
    for (int j = 0; j < n; ++j) {
      // Skip if the column or diagonals are already occupied
      if (cols[j] || diag1[i + j] || diag2[j - i + n - 1])
        continue;

      // Place a queen and mark the column and diagonals as occupied
      board[i][j] = 'Q';
      cols[j] = diag1[i + j] = diag2[j - i + n - 1] = true;

      // Recursively try placing queens in the next row
      dfs(n, i + 1, cols, diag1, diag2, board, ans);

      // Backtrack: remove the queen and reset the availability flags
      cols[j] = diag1[i + j] = diag2[j - i + n - 1] = false;
      board[i][j] = '.';
    }
  }
};
