class Solution {
 public:
  bool isMatch(string s, string p) {
    const int m = s.length();
    const int n = p.length();
    
    // dp[i][j] := true if s[0..i) matches p[0..j)
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    dp[0][0] = true; // Empty string matches empty pattern

    // Lambda function to check character match (handles '.' wildcard)
    auto isMatch = [&](int i, int j) -> bool {
      return j >= 0 && (p[j] == '.' || s[i] == p[j]);
    };

    // Initialize dp for patterns with leading '*' that can match an empty string
    for (int j = 0; j < n; ++j)
      if (p[j] == '*' && dp[0][j - 1])
        dp[0][j + 1] = true;

    // Fill the DP table
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (p[j] == '*') {
          // The minimum index of '*' is 1, so check previous character
          const bool noRepeat = dp[i + 1][j - 1];  // '*' acts as zero occurrences
          const bool doRepeat = isMatch(i, j - 1) && dp[i][j + 1]; // '*' repeats preceding char
          dp[i + 1][j + 1] = noRepeat || doRepeat;
        } 
        else if (isMatch(i, j)) {
          dp[i + 1][j + 1] = dp[i][j]; // Carry forward the match state
        }
      }
    }

    return dp[m][n]; // Return final match result
  }
};
