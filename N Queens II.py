class Solution {
 public:
  int totalNQueens(int n) {
    int ans = 0;
    // Start DFS to count all valid configurations
    dfs(n, 0, vector<bool>(n), vector<bool>(2 * n - 1), vector<bool>(2 * n - 1), ans);
    return ans;
  }

 private:
  void dfs(int n, int i, vector<bool>& cols, vector<bool>& diag1,
           vector<bool>& diag2, int& ans) {
    if (i == n) {
      // If all rows have queens, increment the answer
      ++ans;
      return;
    }

    for (int j = 0; j < n; ++j) {
      // Skip if column or diagonals are already occupied
      if (cols[j] || diag1[i + j] || diag2[j - i + n - 1])
        continue;

      // Mark the current column and diagonals as occupied
      cols[j] = diag1[i + j] = diag2[j - i + n - 1] = true;

      // Recurse to place queens in the next row
      dfs(n, i + 1, cols, diag1, diag2, ans);

      // Backtrack: reset the current column and diagonals
      cols[j] = diag1[i + j] = diag2[j - i + n - 1] = false;
    }
  }
};
