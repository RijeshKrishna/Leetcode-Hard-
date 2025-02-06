class Solution {
 public:
  string longestPalindrome(string s) {
    if (s.empty())  // Edge case: If the string is empty, return an empty string
      return "";

    // (start, end) indices of the longest palindrome found in s
    pair<int, int> indices = {0, 0};

    for (int i = 0; i < s.length(); ++i) {
      // Expand around a single center (odd-length palindrome)
      const auto [l1, r1] = extend(s, i, i);
      if (r1 - l1 > indices.second - indices.first) // Update longest palindrome if needed
        indices = {l1, r1};

      // Expand around two centers (even-length palindrome)
      if (i + 1 < s.length() && s[i] == s[i + 1]) {
        const auto [l2, r2] = extend(s, i, i + 1);
        if (r2 - l2 > indices.second - indices.first)
          indices = {l2, r2};
      }
    }

    // Extract and return the longest palindromic substring
    return s.substr(indices.first, indices.second - indices.first + 1);
  }

 private:
  // Returns the (start, end) indices of the longest palindrome by expanding
  // from the given indices i and j.
  pair<int, int> extend(const string& s, int i, int j) {
    while (i >= 0 && j < s.length() && s[i] == s[j]) {
      --i;
      ++j;
    }
    return {i + 1, j - 1};  // Adjust back to the last valid palindrome indices
  }
};
