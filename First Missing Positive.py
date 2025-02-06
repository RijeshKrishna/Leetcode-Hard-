class Solution {
 public:
  int firstMissingPositive(vector<int>& nums) {
    const int n = nums.size();

    // Correct placement:
    // The number nums[i] should be placed at index nums[i] - 1
    // If nums[i] = i + 1, then nums[nums[i] - 1] = nums[i]
    for (int i = 0; i < n; ++i)
      // Place the number at its correct index if it's between 1 and n
      while (nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1])
        swap(nums[i], nums[nums[i] - 1]);

    // Find the first index where the value is not i + 1, which indicates the missing positive number
    for (int i = 0; i < n; ++i)
      if (nums[i] != i + 1)
        return i + 1;

    // If all indices have the correct numbers, the missing positive is n + 1
    return n + 1;
  }
};
