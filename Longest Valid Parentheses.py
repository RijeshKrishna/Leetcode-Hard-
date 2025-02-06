class Solution {
 public:
  int longestValidParentheses(string s) {
    const string s2 = ")" + s;  // Adding a dummy ')' at the beginning to handle edge cases
    vector<int> dp(s2.length()); // dp[i] stores the longest valid parentheses ending at index i

    for (int i = 1; i < s2.length(); ++i)
      if (s2[i] == ')' && s2[i - dp[i - 1] - 1] == '(') // Valid matching pair found
        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2; // Update dp based on previous values

    return ranges::max(dp); // Return the maximum valid parentheses length
  }
};
