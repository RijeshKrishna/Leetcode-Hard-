class Solution {
 public:
  int trap(vector<int>& height) {
    const int n = height.size();
    int ans = 0;
    
    // Arrays to store the maximum height from the left and right for each position
    vector<int> l(n);  // l[i] := max(height[0..i])
    vector<int> r(n);  // r[i] := max(height[i..n))

    // Fill left array with maximum height encountered up to each position
    for (int i = 0; i < n; ++i)
      l[i] = (i == 0) ? height[i] : max(height[i], l[i - 1]);

    // Fill right array with maximum height encountered from each position to the end
    for (int i = n - 1; i >= 0; --i)
      r[i] = (i == n - 1) ? height[i] : max(height[i], r[i + 1]);

    // Calculate the trapped water by checking the min height between the left and right minus current height
    for (int i = 0; i < n; ++i)
      ans += min(l[i], r[i]) - height[i];

    return ans;  // Return the total amount of water trapped
  }
};
