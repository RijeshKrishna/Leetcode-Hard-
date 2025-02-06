class Solution {
 public:
  bool isMatch(string s, string p) {
    const int m = s.length();
    const int n = p.length();
    
    // dp[i][j] := true if s[0..i) matches p[0..j)
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1));
    dp[0][0] = true;

    // Helper lambda to check if characters match considering '?' wildcard
    auto isMatch = [&](int i, int j) -> bool {
      return (j >= 0 && p[j] == '?') || s[i] == p[j];  // '?' matches any single character
    };

    // Handle '*' in pattern p for empty matching at the start
    for (int j = 0; j < n; ++j)
      if (p[j] == '*')
        dp[0][j + 1] = dp[0][j];  // '*' can match an empty string

    // Dynamic programming approach to check if substrings match
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (p[j] == '*') {
          // '*' can match either an empty string (move to next in pattern) or one character (move to next in string)
          const bool matchEmpty = dp[i + 1][j];  // Skip the '*' in pattern
          const bool matchSome = dp[i][j + 1];  // Skip one character in string
          dp[i + 1][j + 1] = matchEmpty || matchSome;
        } else if (isMatch(i, j)) {
          // For '?' or exact matches, propagate the result from the previous state
          dp[i + 1][j + 1] = dp[i][j];
        }

    // Final result at the bottom-right corner of the dp table
    return dp[m][n];
  }
};
